# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_ingestion.manual.src.contracts.ISPTokenProvider import ISPTokenProvider
from azext_ingestion.manual.src.contracts.IUserTokenProvider import IUserTokenProvider
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
def get_token(cmd, client:ISPTokenProvider, azure_tenent:str, service_principal:str, service_principal_secret:str, configuration_file:str):
    client.prepare(azure_tenent, service_principal, service_principal_secret, configuration_file)
    return client.acquire_token()

def get_user_token(cmd, client:IUserTokenProvider, scope:str):
    #refresh = "0.ARoAv4j5cvGGr0GRqy180BHbR1xIGCFCSNtDsB1OeiE2cNgaAEM.AgABAAEAAAD--DLA3VO7QrddgJg7WevrAgDs_wQA9P-MspfGA4XYo01wv5LC163iSE0Q_KWqbDxHKwhqk7YiM8BsZvAJqQQPEm3oCT53WM5Gl0aOgsJvFjaIx0MjgkYXJC0Cxwb26eJb3fpD9aJGpSi8-aEm2OhGXfFe4PoyxPZW-KCuotg0SNeYnk5fYZdklOE3rqmjwKQ8CzqRtI-xJQaXElYuA8JWioio8VMNCNeGEopfcJIoaGLqTDiSWEAeoqPYgoEe08pIl-bDonbgYsE37_UnQd-2MDIdl37SuOIrslpMbSCXdonZjQ_FokI1Ndif2sWKCrYz63E8GX43h4sQGDGIsNkMeNveSel8_4lUzhgdSVDYIrl3fsJOBFP-7TZRja1Lvg5NjY4cu4R4MAtLMAIht9HyiJHC3bqlAiRWhYq1b978w2YTXl1rqGy-E7pQ67PpGM_XrhIzYAaalgkzAmsad-RfeKXXLJdithgxeDcTEUpCTEz304LgI9JRjwGZdArBeoeUtsTcNVx4wb5vokhfhHLAXo0zHofGur20AqiI_r3IiALdCN-jn8cf_oZzOZISDeTL0ooOm4tAEcySVmuhp5Mo4_eLDIDntlZzuJ0faJ_2FZwmiN3QHMfPVIbtjjUQCLjnSdqwfHg7x2MhAHjIgzNU3sBbqWy1jkDuXO75U6DF0oJEfsGhwNnCVYod3OsrPmBqkhcSGvlCtRtQXLrbRH-dfH0g_7rD_hsAph78664wWCgbhVsikxTxvnqt1TgBFV2xUWiJUJjhN0Pz_MHhQNxkEonofzniDGy81t7Ii3nql9cyEueuF-QemZCxRbZhSVlWeBQqpMF8lxsjVuKUdkLBRB8yDJm69zxN_TqVvpVnqJ-aGLe3RR6n0kHYX_dGid0Aq296wNv1fn2u_iF7-PE17iC5moOPtwATZMZ4PotB9ltGLefo5bB4QZqxZwR0kM6QKHugMNMiboF_4d-y5S2yiW9wxWJHvqE6TLfoFHay9IoPYIC-BtXkcbNr6VpY49PKKh7F3RkvcFlFNzFNejFrMCzXKs_Dupcemi-qzZirkbcBJLlf_1fAoQ-OwOjKyvZZT5Wf4p1lv5jXNIdOvFjSX1HfQp-P-zF7mzzQbFeC8-Z5_ISKVWfN"
    #dev_portal = "https://experiencelab1000.azurewebsites.net"
    #client_id = "2118485c-4842-43db-b01d-4e7a213670d8"

    #print("REFRESHED")
    #t = client.acquire_platform_token(refresh, client_id, dev_portal)
    #return t
    return client.acquire_token(scope)

def get_platform_token(cmd, client:IUserTokenProvider, service_principal:str, dev_platform:str, refresh_token:str):
    return client.acquire_platform_token(refresh_token, service_principal, dev_platform)

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
