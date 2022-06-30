# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
from azext_energy.command_const import CommandConstants

############################################
# Help commands for our commands and sub group
# commands.
############################################

helps['{}'.format(CommandConstants.ROOT)] = """
    type: group
    short-summary: Commands to manage Energy Platform.
"""

helps['{} create'.format(CommandConstants.ROOT)] = """
    type: command
    short-summary: Create a Energy.
"""

helps['{} list'.format(CommandConstants.ROOT)] = """
    type: command
    short-summary: List Energy.
"""

# Help for sub command energy token - get
helps['{} auth sp'.format(CommandConstants.ROOT)] = """
    type: command
    short-summary: Get authentication token for service principal.
    examples:
      - name: Acquire service principal token
        text: |-
                Token can be acquired by providing the configuration direction or by providing a 
                configuration json file with the settings contained within it. 

                az energy auth sp --tenent "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                                  --service-principal "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                                  --service-principal-credential "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                or
                
                Supply a configuration file, as a json dictionry, with the above fields. 
                
                az energy auth sp --configuration "local_json_with_settings"
"""

helps['{} auth platform'.format(CommandConstants.ROOT)] = """
    type: command
    short-summary: Get authentication token from existing platform refresh token
    examples:
      - name: Acquire platform token
        text: |-

                az energy auth platform --service-principal "principal id used to generate original token"
                                        --dev-portal "Experience Lab development portal url"
                                        --refresh-token "Refresh token to use"
"""

helps['{} auth user'.format(CommandConstants.ROOT)] = """
    type: command
    short-summary: Get authentication token for current user.
    examples:
      - name: Acquire user token
        text: |-

                az energy auth user --scope "https://management.azure.com/.default"
"""

helps['{} platform add'.format(CommandConstants.ROOT)] = """
    type: command
    short-summary: Adds an OSDU platform configuration to cli settings.
    examples:
      - name: Adds a platform to the internal settings to be used later.
        text: |-
                File format is JSON and MUST contain the following fields:

                {
                    "name" : "Platform name, spaces require quotes when show/remove called",
                    "type" : "platform",
                    "url" : "Base Url of the OSDU platform",
                    "data_partition" : "Name of the data partition to use",
                    "api_path" : {
                        "ENTITLEMENTS_HOST" : "/api/entitlements/v2",
                        "LEGAL_HOST" : "/api/legal/v1",
                        "SCHEMA_HOST" : "/api/schema-service/v1",
                        "STORAGE_HOST" : "/api/storage/v2",
                        "SEARCH_HOST" : "/api/search/v2",
                        "WORKLFOW_HOST" : "/api/workflow/v1",
                        "FILE_HOST" : "/api/file/v2",
                        "PARTITION_HOST" : "/api/partition/v1",
                        "REGISTER_HOST" : "/api/register/v1"        
                    }
                }
"""

helps['{} utility add'.format(CommandConstants.ROOT)] = """
    type: command
    short-summary: Adds a utility configuration to the settings.
    examples:
      - name: Adds a utility to the internal settings to be used later.
        text: |-
                XXX File format is JSON and MUST contain the following fields:

                {
                    "name" : "Platform name, spaces require quotes when show/remove called",
                    "type" : "utility",
                    "others" : "not validated"
                }
"""


