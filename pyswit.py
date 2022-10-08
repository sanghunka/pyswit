import requests
import json


__version__ = "0.0.1"


class BaseAPI:
    base_url = "https://openapi.swit.io/v1/api"

    def __init__(self, access_token):
        self.access_token = access_token
        self.api_url = f"{self.base_url}/{self.__class__.__name__.lower()}"

    def get_endpoint(self):
        return f"{self.api_url}/{self.__class__.__name__.lower()}"

    def get_headers(self, accept=None, content_type=None):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        if accept:
            headers.update({"Accept": accept})
        if content_type:
            headers.update({"Content-Type": content_type})
        return headers
