# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .contracts.IPersistConfiguration import IPersistConfiguration


class UtilityPersistConfiguration(IPersistConfiguration):
    """
    Tools have not specified format, so it's a free for all here. 
    """

    # File name for storage
    TOOL_CONF_DATA = "utility_conf.json"

    def __init__(self):
        super().__init__(None, UtilityPersistConfiguration.TOOL_CONF_DATA)
        self.configuration = {}

    def get_section(self, section_name:str) -> dict:
        """Get a section, return None if not found"""
        return (
            self.configuration[section_name]
            if section_name in self.configuration
            else None
        )
    
    def put_section(self, section_name:str, data:dict) -> None:
        """Put a section, if data is none, remove it."""
        if not data and section_name in self.configuration:
            del self.configuration[section_name]
        elif data and section_name:
            self.configuration[section_name] = data

        self.save_configuration()

    def get_configuration(self) -> None:
        data = super().get_configuration()
        self.configuration = data or {}
        return self.configuration

    def save_configuration(self) -> None:
        super().save_configuration(self.configuration)

