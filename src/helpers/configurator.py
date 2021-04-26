"""Module with configs"""
import settings
import configparser

class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file_name = f"{settings.ROOT_DIR}/config.ini"
        self.config.read(self.file_name)


    def create_section(self, section_name: str):
        self.config[section_name]={}
        self.save_config_file()

    def create_section_values(self, section_name: str, values_dict: dict):
        if section_name not in self.config.sections():
            self.config.add_section(section_name)
        for key, value in values_dict.items():
            self.config.set(section_name, key, value)
        self.save_config_file()

    def save_config_file(self):
        with open(self.file_name , 'w') as configfile:
            self.config.write(configfile)

    def get_config_value(self, section: str, key: str):
        return self.config.get(section=section, option=key)
