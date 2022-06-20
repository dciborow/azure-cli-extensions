# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
from pathlib import Path
import os
import json
from knack.util import CLIError


class IPersistConfiguration(ABC):

    EXTENSION_ROOT = ".azext_ingestion"
    SECTION_NAME = "name"

    def __init__(self, sub_path: str, file_name:str):
        self.sub_path = sub_path
        self.file_name = file_name

    def get_local_root(self) -> str:
        return os.path.join(str(Path.home()), IPersistConfiguration.EXTENSION_ROOT)

    def get_configuration(self) -> dict:
       
        return_data = None

        if not self.file_name:
            raise CLIError("Configuration file is required.")

        path = None
        if self.sub_path:
            path = os.path.join(self.get_local_root(), self.sub_path, self.file_name)
        else:
            path = os.path.join(self.get_local_root(), self.file_name)


        if os.path.exists(path):
            try:
                with open(path, "r") as configuration_file:
                    data = configuration_file.readlines()
                    data = "\n".join(data)
                    return_data = json.loads(data)

            except Exception as ex:
                raise CLIError("Configuruation load error ({}): {}".format(path, str(ex)))

        return return_data

    def save_configuration(self, data:dict) -> None:

        if not self.file_name:
            raise CLIError("Configuration file is required.")

        path = None
        if self.sub_path:
            path = os.path.join(self.get_local_root(), self.sub_path)
        else:
            path = self.get_local_root()

        if not os.path.exists(path):
            os.makedirs(path)

        path = os.path.join(path, self.file_name)

        if not data:
            if os.path.exists(path):
                os.remove(path)
        else:
            written_data = json.dumps(data, indent=4)
            with open(path, "w") as configuration_file:
                configuration_file.writelines(written_data)

    @abstractmethod
    def get_section(self, section_name:str) -> dict:
        """Get a section, return None if not found"""
    
    @abstractmethod
    def put_section(self, section_name:str, data:dict) -> None:
        """Put a section, if data is none, remove it."""

    @staticmethod
    def load_configuration(configuration_file:str, as_json:bool) -> object:

        if not os.path.exists(configuration_file):
            raise CLIError("Configuration file missing: {}".format(configuration_file))
       
        settings = None    
       
        with open(configuration_file, "r") as configuration:
            settings = configuration.readlines()
            if as_json:
                settings = "\n".join(settings)
                settings = json.loads(settings)
        
        return settings