# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .contracts.IPersistConfiguration import IPersistConfiguration
from knack.util import CLIError


class OSDUPersistConfiguration(IPersistConfiguration):
    """
    Platform configuration holds information for any number of platforms in a JSON file 
    [
        {
            "name" : platform name
            "url" : platform url
            "data_partition" : partition name
            "api_path: : {
                All or subset of the following host endpoints aligned with 
                the platform itself. 
            }

        }
    ]
    Api Path Examples

    @ENTITLEMENTS_HOST = {{ENDPOINT}}/api/entitlements/v2
    @LEGAL_HOST = {{ENDPOINT}}/api/legal/v1
    @SCHEMA_HOST = {{ENDPOINT}}/api/schema-service/v1
    @STORAGE_HOST = {{ENDPOINT}}/api/storage/v2
    @SEARCH_HOST = {{ENDPOINT}}/api/search/v2
    @WORKLFOW_HOST = {{ENDPOINT}}/api/workflow/v1
    @FILE_HOST = {{ENDPOINT}}/api/file/v2
    @PARTITION_HOST = {{ENDPOINT}}/api/partition/v1
    @REGISTER_HOST = {{ENDPOINT}}/api/register/v1
    """

    # Root level values
    PLATFORM_NAME = "name"
    PLATFORM_URL = "url"
    PLATFORM_PARTITION = "data_partition"
    PLATFORM_API = "api_path"

    PLATFORM_VALIDATION = [
        PLATFORM_NAME,
        PLATFORM_URL,
        PLATFORM_PARTITION,
        PLATFORM_API
    ]

    # endpoints
    ENTITLEMENTS_HOST = "ENTITLEMENTS_HOST"
    LEGAL_HOST = "LEGAL_HOST"
    SCHEMA_HOST = "SCHEMA_HOST"
    STORAGE_HOST = "STORAGE_HOST"
    SEARCH_HOST = "SEARCH_HOST"
    WORKLFOW_HOST = "WORKLFOW_HOST"
    FILE_HOST = "FILE_HOST"
    PARTITION_HOST = "PARTITION_HOST"
    REGISTER_HOST = "REGISTER_HOST"

    # File name for storage
    OSDU_CONF_DATA = "platform_conf.json"

    def __init__(self):
        super().__init__(None, OSDUPersistConfiguration.OSDU_CONF_DATA)
        self.configuration = {}

    def get_section(self, section_name:str) -> dict:
        """Get a section, return None if not found"""
        return_value = None
        if section_name in self.configuration:
            return_value = self.configuration[section_name]
        return return_value
    
    def put_section(self, section_name:str, data:dict) -> None:
        """Put a section, if data is none, remove it."""
        if not data and section_name in self.configuration:
            del self.configuration[section_name]
        elif data and section_name:
            for field in OSDUPersistConfiguration.PLATFORM_VALIDATION:
                if field not in data:
                    raise CLIError("Required field missing in configuration: {}".format(field))

            self.configuration[section_name] = data

        self.save_configuration()

    def get_configuration(self) -> None:
        data = super().get_configuration()
        if not data:
            self.configuration = {}
        else:
            self.configuration = data
        return self.configuration

    def save_configuration(self) -> None:
        super().save_configuration(self.configuration)

