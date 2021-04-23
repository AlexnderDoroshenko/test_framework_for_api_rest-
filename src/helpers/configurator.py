"""Module with configs"""

import configparser


class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file_name = "../resource.config.ini"


    def create_section(self, section_name: str):
        self.config[section_name]={}
        self.save_config_file()

    def create_section_values(self, section_name: str, values_dict: dict):
        self.config.add_section(section_name)
        for key, value in values_dict.items():
            self.config.set(section_name, key, value)
        self.save_config_file()

    def save_config_file(self):
        with open(self.file_name , 'w') as configfile:
            self.config.write(configfile)



con = Config()

con.create_section_values("api", {"url": "https://gorest.co.in/public-api/users"})