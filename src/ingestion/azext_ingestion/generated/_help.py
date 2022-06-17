# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

############################################
# Help commands for our commands and sub group
# commands.
############################################

helps['ingestion'] = """
    type: group
    short-summary: Commands to manage Ingestions.
"""

helps['ingestion create'] = """
    type: command
    short-summary: Create a Ingestion.
"""

helps['ingestion list'] = """
    type: command
    short-summary: List Ingestions.
"""

# Help for sub command ingestion token - get
helps['ingestion token get'] = """
    type: command
    short-summary: Get authentication token.
    examples:
      - name: Acquire platform token
        text: |-
                Token can be acquired by providing the configuration direction or by providing a 
                configuration json file with the settings contained within it. 

                az ingestion token --tenent "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                                  --service-principal "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                                  --service-principal-credential "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                or
                
                Supply a configuration file, as a json dictionry, with the above fields. 
                
                az ingestion token --configuration "local_json_with_settings"
"""

# helps['ingestion delete'] = """
#     type: command
#     short-summary: Delete a Ingestion.
# """

# helps['ingestion show'] = """
#     type: command
#     short-summary: Show details of a Ingestion.
# """

# helps['ingestion update'] = """
#     type: command
#     short-summary: Update a Ingestion.
# """
