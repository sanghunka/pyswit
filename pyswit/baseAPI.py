import requests
import json
import inspect


class BaseAPI:
    api_url = "https://openapi.swit.io/v1/api"

    def __init__(self, access_token: str, endpoint: str = None):
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

    def get_headers(
        self, accept: str = None, content_type: str = None, authorization: bool = True
    ):
        if authorization:
            headers = {"Authorization": f"Bearer {self.access_token}"}
        else:
            headers = {}

        if accept:
            headers.update({"Accept": accept})
        if content_type:
            headers.update({"Content-Type": content_type})
        return headers

    def params_to_dict(self, params: dict):
        if "self" in params:
            del params["self"]
        params_without_none = {k: v for k, v in params.items() if v is not None}
        return params_without_none

    def get(self, url: str, headers: dict, data: dict = None, params: dict = None):
        r = requests.get(url=url, headers=headers, json=data, params=params)
        return json.loads(r.content)

    def post(self, url: str, headers: dict, data: dict = None):
        if headers["Content-Type"] == "application/json":
            r = requests.post(url=url, headers=headers, json=data)
        if headers["Content-Type"] == "application/x-www-form-urlencoded":
            r = requests.post(url=url, headers=headers, data=data)

        if r.status_code == 204:
            return {"data": [{}]}
        return json.loads(r.content)
