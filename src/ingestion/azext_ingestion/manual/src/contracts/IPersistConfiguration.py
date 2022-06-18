from abc import ABC, abstractmethod
from pathlib import Path
import os
import json
from knack.util import CLIError

class IPersistConfiguration(ABC):

    def get_local_root(self) -> str:
        return str(Path.home())

    def get_configuration(self, directory:str, file:str) -> dict:

        return_data = None

        if not directory:
            raise CLIError("Directory is required to acquire configuration file.")
        if not file:
            raise CLIError("Configuration file is required.")

        path = os.path.join(self.get_local_root(), directory, file)

        if os.path.exists(path):
            try:
                with open(path, "r") as configuration_file:
                    data = configuration_file.readlines()
                    data = "\n".join(data)
                    return_data = json.loads(data)

            except Exception as ex:
                raise CLIError("Configuruation load error ({}): {}".format(path, str(ex)))

        return return_data

    def save_configuration(self, directory:str, file:str, data:dict) -> None:

        return_data = None

        if not directory:
            raise CLIError("Directory is required to acquire configuration file.")
        if not file:
            raise CLIError("Configuration file is required.")

        path = os.path.join(self.get_local_root(), directory)

        if not os.path.exists(path):
            os.makedirs(path)

        path = os.path.join(path, file)

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
