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


class User(BaseAPI):
    def info(self):
        headers = self.get_headers()
        r = requests.get(
            "https://openapi.swit.io/v1/api/user.info",
            headers=headers,
            json=None,
        )
        return json.loads(r.content)


class Message(BaseAPI):
    def create(self, channel_id, content):
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        data_obj = {"channel_id": channel_id, "content": content}

        r = requests.post(
            "https://openapi.swit.io/v1/api/message.create",
            headers=headers,
            json=data_obj,
        )
        return json.loads(r.content)


class Pyswit:
    def __init__(self, access_token):
        api_args = {"access_token": access_token}

        self.user = User(**api_args)
        self.message = Message(**api_args)
