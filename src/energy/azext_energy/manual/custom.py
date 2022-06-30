# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_energy.manual.src.contracts.ISPTokenProvider import ISPTokenProvider
from azext_energy.manual.src.contracts.IUserTokenProvider import IUserTokenProvider
from azext_energy.manual.src.contracts.IPersistConfiguration import IPersistConfiguration
from azext_energy.manual.src._tool_executioner import ToolExecutionContext, ToolExecutionContent

""" Original template unused
def create_energy(cmd, client, resource_group_name, energy_name, location=None, tags=None):
    raise CLIError('TODO: Implement `energy create`')


def list_energy(cmd, client, resource_group_name=None):
    raise CLIError('TODO: Implement `energy list` darn it')

def update_energy(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance
"""

############################################
# Token
############################################
def get_token(cmd, client:ISPTokenProvider, azure_tenent:str, service_principal:str, service_principal_secret:str, configuration_file:str):
    client.prepare(azure_tenent, service_principal, service_principal_secret, configuration_file)
    return client.acquire_token()

def get_user_token(cmd, client:IUserTokenProvider, scope:str):
    return client.acquire_token(scope)

def get_platform_token(cmd, client:IUserTokenProvider, service_principal:str, dev_platform:str, refresh_token:str):
    return client.acquire_platform_token(refresh_token, service_principal, dev_platform)

############################################
# Platform Configuration
############################################
def list_platforms(cmd, client:IPersistConfiguration):
    return client.get_configuration()

def add_platform(cmd, client:IPersistConfiguration, configuration_file:str):
    client.get_configuration()
    
    platform_settings = IPersistConfiguration.load_configuration(configuration_file, True)
    IPersistConfiguration.validate_requirements(platform_settings, IPersistConfiguration.PERSIST_TYPE_PLATFORM)

    client.put_section(platform_settings[IPersistConfiguration.NAME_PROP], platform_settings)
    return list_platforms(None, client)

def show_platform(cmd, client:IPersistConfiguration, platform_name):
    client.get_configuration()
    platform = client.get_section(platform_name)
    if not platform:
        print("Platform {} not found".format(platform_name))
    return platform

def remove_platform(cmd, client:IPersistConfiguration, platform_name):
    conf = client.get_configuration()
    if platform_name in conf:
        client.put_section(platform_name, None)

############################################
# Utility Configuration
############################################
def list_utility(cmd, client:IPersistConfiguration):
    return client.get_configuration()

def add_utility(cmd, client:IPersistConfiguration, configuration_file:str):
    client.get_configuration()
    
    platform_settings = IPersistConfiguration.load_configuration(configuration_file, True)
    IPersistConfiguration.validate_requirements(platform_settings, IPersistConfiguration.PERSIST_TYPE_UTILITY)

    client.put_section(platform_settings[IPersistConfiguration.NAME_PROP], platform_settings)
    return list_platforms(None, client)

def show_utility(cmd, client:IPersistConfiguration, utility_name):
    client.get_configuration()
    utility = client.get_section(utility_name)
    if not utility:
        print("Utility {} not found".format(utility_name))
    return utility

def remove_utility(cmd, client:IPersistConfiguration, utility_name):
    conf = client.get_configuration()
    if utility_name in conf:
        client.put_section(utility_name, None)


############################################
# Tool Execution
############################################

def _get_utility_content(client:ToolExecutionContext, platform_name, utility_name, configuration_file) -> ToolExecutionContent:
    return_content = ToolExecutionContent()

    return_content.platform = show_platform(None, client.platform_config, platform_name)
    if not return_content.platform:
        raise CLIError("Platform is an invalid target for job: {}".format(platform_name))

    # Obtain the tool settings from persistance
    return_content.tool = show_utility(None, client.tool_config, utility_name)
    if not return_content.tool:
        raise CLIError("Utility is an invalid target for job: {}".format(utility_name))

    return_content.tool_params = IPersistConfiguration.load_configuration(configuration_file, True)
    if not return_content.tool_params:
        raise CLIError("Job configuration is an invalid target for job: {}".format(configuration_file))
    IPersistConfiguration.validate_requirements(return_content.tool_params, IPersistConfiguration.PERSIST_TYPE_JOB)

    return return_content

def execute_utility(cmd, client:ToolExecutionContext, platform_name, utility_name, configuration_file):
    job_content:ToolExecutionContent = _get_utility_content(client, platform_name, utility_name, configuration_file)
    client.executor.execute("foobarauth", job_content.platform, job_content.tool, job_content.tool_params)
