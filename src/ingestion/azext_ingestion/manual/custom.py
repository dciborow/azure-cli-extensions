# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
from platform import platform
from knack.util import CLIError
from azext_ingestion.manual.src.contracts.ITokenProvider import ITokenProvider
from azext_ingestion.manual.src.contracts.IPersistConfiguration import IPersistConfiguration

def create_ingestion(cmd, client, resource_group_name, ingestion_name, location=None, tags=None):
    raise CLIError('TODO: Implement `ingestion create`')


def list_ingestion(cmd, client, resource_group_name=None):
    raise CLIError('TODO: Implement `ingestion list` darn it')

def update_ingestion(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance

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
    
    platform_settings = None
    with open(configuration_file, "r") as configuration:
        platform_settings = configuration.readlines()
        platform_settings = "\n".join(platform_settings)
        platform_settings = json.loads(platform_settings)
    
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
        print("Found it")
        client.put_section(platform_name, None)
