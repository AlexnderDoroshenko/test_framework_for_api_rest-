import logging


class Logger:
    def __init__(self):
        self.log = logging
        self.file_name = "api.log"
        self.basic = self.log.basicConfig(filename='app.log',
                                          filemode='w',
                                          format='%(name)s - %(levelname)s - %(message)s')

    def set_log_format(self, format_str: str):
        self.basic(format=format_str)
        return self

    def set_log_date_format(self, format_str: str):
        self.basic(datefmt=format_str)
        return self

    def set_log_level(self, level_str: str):
        self.basic(level=level_str)
        return self



