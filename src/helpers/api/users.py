from src.helpers.configurator import Config
from src.helpers.logging import Logger
import requests
import json
import settings

class Users:
    def __init__(self):
        self.config = Config()
        # self.api_url = self.config.get_config_value('api','url')  # Or you can take it from settings.BASE_URL
        self.api_url = settings.BASE_URL
        self.logger = Logger().set_log_level("DEBUG")
        self.request = requests
        self.token = f"Bearer {self.config.get_config_value('test', 'api_token')}"
        self.header = {"Authorization": self.token,
                       "COntent-Type": "application/json"}
        self.verify = True

    def get_user(self, user_id: int):
        try:
            return self.request.get(url=f"{self.api_url}/{user_id}", verify=self.verify)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def put_user(self, user_id: int, body: dict):
        try:
            return self.request.put(url=f"{self.api_url}/{user_id}", data=json.dumps(body),
                             headers=self.header, verify=self.verify)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def patch_user(self, user_id: int, body: dict):
        try:
            return self.request.patch(url=f"{self.api_url}/{user_id}", data=json.dumps(body),
                             headers=self.header, verify=self.verify)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def delete_user(self, user_id: int):
        try:
            return self.request.delete(url=f"{self.api_url}/{user_id}", headers=self.header, verify=self.verify)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def post_user(self, body: dict):
        try:
            return self.request.post(url=self.api_url, data=json.dumps(body), headers=self.header, verify=self.verify)
        except Exception as e:
            print(f"Error :{e}")
            # self.logger.log.debug("Exception occurs", exc_info=True)

    def options_user(self, user_id: int):
        try:
            return self.request.options(url=self.api_url)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)

    def head_user(self, user_id: int):
        try:
            return self.request.head(
                         url=self.api_url)
        except Exception as e:
            self.logger.log.debug("Exception occurs", exc_info=True)
