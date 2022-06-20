# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_ingestion.manual.src.contracts.ITokenProvider import ITokenProvider
from azext_ingestion.manual.src.contracts.IPersistConfiguration import IPersistConfiguration
from azext_ingestion.manual.src._tool_executioner import ToolExecutionContext

""" Original template unused
def create_ingestion(cmd, client, resource_group_name, ingestion_name, location=None, tags=None):
    raise CLIError('TODO: Implement `ingestion create`')


def list_ingestion(cmd, client, resource_group_name=None):
    raise CLIError('TODO: Implement `ingestion list` darn it')

def update_ingestion(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance
"""

############################################
# Token
############################################
def get_token(cmd, client:ITokenProvider, azure_tenent:str, service_principal:str, service_principal_secret:str, configuration_file:str):
    client.prepare(azure_tenent, service_principal, service_principal_secret, configuration_file)
    return client.acquire_token()

############################################
# Platform Configuration
############################################
def list_platforms(cmd, client:IPersistConfiguration):
    config = client.get_configuration()
    if not config:
        config = {}
    return config

def add_platform(cmd, client:IPersistConfiguration, configuration_file:str):
    client.get_configuration()
    
    platform_settings = IPersistConfiguration.load_configuration(configuration_file, True)
    if IPersistConfiguration.SECTION_NAME not in platform_settings:
        raise CLIError("Platform name is missing from configuration {}".format(configuration_file))

    client.put_section(platform_settings[IPersistConfiguration.SECTION_NAME], platform_settings)
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
# Tool Configuration
############################################
def list_tools(cmd, client:IPersistConfiguration):
    config = client.get_configuration()
    if not config:
        config = {}
    return config

def add_tool(cmd, client:IPersistConfiguration, configuration_file:str):
    client.get_configuration()
    
    platform_settings = IPersistConfiguration.load_configuration(configuration_file, True)
    if IPersistConfiguration.SECTION_NAME not in platform_settings:
        raise CLIError("Platform name is missing from configuration {}".format(configuration_file))

    client.put_section(platform_settings[IPersistConfiguration.SECTION_NAME], platform_settings)
    return list_platforms(None, client)

def show_tool(cmd, client:IPersistConfiguration, tool_name):
    client.get_configuration()
    tool = client.get_section(tool_name)
    if not tool:
        print("Tool {} not found".format(tool_name))
    return tool

def remove_tool(cmd, client:IPersistConfiguration, tool_name):
    conf = client.get_configuration()
    if tool_name in conf:
        client.put_section(tool_name, None)


############################################
# Tool Execution
############################################
def execute_tool(cmd, client:ToolExecutionContext, platform_name, tool_name, configuration_file):

    # Obtain the platform settings from persistance
    platform = show_platform(None, client.platform_config, platform_name)
    if not platform:
        raise CLIError("Platform is an invalid target for job: {}".format(platform_name))

    # Obtain the tool settings from persistance
    tool = show_tool(None, client.tool_config, tool_name)
    if not tool:
        raise CLIError("Tool is an invalid target for job: {}".format(tool_name))

    # Load the job configuration as JSON (fails if not json)
    job = IPersistConfiguration.load_configuration(configuration_file, True)
    if not job:
        raise CLIError("Job configuration is an invalid target for job: {}".format(configuration_file))

    # Execute the job...this will likely be different as jobs expand. 
    client.executor.execute("foobarauth", platform, tool, job)
