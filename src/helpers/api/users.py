from src.helpers.configurator import Config
from src.helpers.logging import Logger
import requests

class Users:
    def __init__(self):
        self.config = Config()
        self.api_url = self.config.get(['api']['url'])
        self.logger = Logger().set_log_level("DEBUG")
        self.request = requests.request

    def get_user(self, user_id: int):
        try:
            self.request(method="GET",
                         url=f"{self.api_url}/{user_id}")
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def put_user(self, user_id: int):
        try:
            self.request(method="PUT",
                         url=f"{self.api_url}/{user_id}")
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def patch_user(self, user_id: int):
        try:
            self.request(method="PATCH",
                         url=f"{self.api_url}/{user_id}")
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def delete_user(self, user_id: int):
        try:
            self.request(method="DELETE",
                         url=f"{self.api_url}/{user_id}")
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def post_user(self):
        try:
            self.request(method="POST",
                         url=self.api_url)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def options_user(self, user_id: int):
        try:
            self.request(method="OPTIONS",
                         url=self.api_url)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def head_user(self, user_id: int):
        try:
            self.request(method="HEAD",
                         url=self.api_url)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)
