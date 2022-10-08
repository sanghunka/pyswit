import requests
import json
import inspect


__version__ = "0.0.1"


class BaseAPI:
    api_url = "https://openapi.swit.io/v1/api"

    def __init__(self, access_token, endpoint=None):
        self._class_name = self.__class__.__name__.lower()
        self.access_token = access_token
        if endpoint:
            self.endpoint = f"{endpoint}.{self._class_name}"
        else:
            self.endpoint = self._class_name

    def get_endpoint_url(self):
        cframe = inspect.currentframe()
        outer_func_name = inspect.getframeinfo(cframe.f_back).function
        return f"{self.api_url}/{self.endpoint}.{outer_func_name}"

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
            url=self.get_endpoint_url(),
            headers=headers,
            json=None,
        )
        return json.loads(r.content)


class Message(BaseAPI):
    def __init__(self, access_token):
        super().__init__(access_token=access_token)

    def create(self, channel_id, content):
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        data_obj = {"channel_id": channel_id, "content": content}

        r = requests.post(
            url=self.get_endpoint_url(),
            headers=headers,
            json=data_obj,
        )
        return json.loads(r.content)


class Pyswit:
    def __init__(self, access_token):
        api_args = {"access_token": access_token}

        self.user = User(**api_args)
        self.message = Message(**api_args)
