from .contracts.IPersistConfiguration import IPersistConfiguration


class OSDUPersistConfiguration(IPersistConfiguration):

    OSDU_CONF_PATH = "OSDUConf"
    OSDU_CONF_DATA = "configuration.json"

    def __init__(self):
        super().__init__(OSDUPersistConfiguration.OSDU_CONF_PATH, OSDUPersistConfiguration.OSDU_CONF_DATA)
        self.configuration = {}

    def get_section(self, section_name:str) -> dict:
        """Get a section, return None if not found"""
    
    def put_section(self, section_name:str, data:dict) -> None:
        """Put a section, if data is none, remove it."""

    def get_configuration(self) -> None:
        data = super().get_configuration()
        if not data:
            self.configuration = {}
        else:
            self.configuration = data
        return self.configuration

    def save_configuration(self) -> None:
        super().save_configuration(self.configuration)

