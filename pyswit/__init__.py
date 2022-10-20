import requests
import json
import inspect


__version__ = "0.0.7"


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

    def get_headers(self, accept: str = None, content_type: str = None):
        headers = {"Authorization": f"Bearer {self.access_token}"}
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
        r = requests.post(url=url, headers=headers, json=data)
        if r.status_code == 204:
            return {"data": [{}]}
        return json.loads(r.content)


class User(BaseAPI):
    def info(self):
        return self.get(url=self.get_endpoint_url(), headers=self.get_headers())


class Workspace(BaseAPI):
    class User(BaseAPI):
        def info(self, workspace_id: str, user_id: str = None):
            params = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(accept="application/json")
            return self.get(url=url, headers=headers, params=params)

        def list(self, workspace_id: str, limit: int = None, offset: str = None):
            params = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(accept="application/json")
            return self.get(url=url, headers=headers, params=params)

        def update(
            self,
            workspace_id: str,
            department: str = None,
            name: str = None,
            status_msg: str = None,
            tel: str = None,
        ):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

    def __init__(self, access_token: str):
        super().__init__(access_token=access_token)
        self.user = self.User(access_token=access_token, endpoint=self._class_name)

    def info(self, id: str):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def list(self, offset: str = None, limit: int = None):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def update(self, id: str, name: str):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)


class Channel(BaseAPI):
    def archive(self, id: str, archive: bool = None):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def create(
        self,
        workspace_id: str,
        name: str,
        description: str = None,
        is_prev_chat_visible: bool = None,
        is_private: bool = None,
    ):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def createDirect(self, user_id: str, workspace_id: str):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def info(self, id: str):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def list(
        self,
        workspace_id: str,
        limit: int = None,
        offset: str = None,
        activity: str = None,
        disclosure: str = None,
        type: str = None,
    ):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def update(
        self,
        id: str,
        description: str = None,
        is_prev_chat_visible: bool = None,
        name: str = None,
    ):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)


class Message(BaseAPI):
    class Comment(BaseAPI):
        def create(self, message_id: str, content: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

        def list(self, message_id: str, offset: str = None, limit: int = None):
            params = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers()
            return self.get(url=url, headers=headers, params=params)

        def remove(self, id: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

    class Reaction(BaseAPI):
        def create(self, message_id: str, reaction_name: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

        def remove(self, message_id: str, reaction_name: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

    def __init__(self, access_token: str):
        super().__init__(access_token=access_token)
        self.comment = self.Comment(
            access_token=access_token, endpoint=self._class_name
        )
        self.reaction = self.Reaction(
            access_token=access_token, endpoint=self._class_name
        )

    def create(self, channel_id: str, content: str):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def info(self, id: str):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers()
        return self.get(url=url, headers=headers, params=params)

    def list(self, channel_id: str, offset: str = None, limit: int = None):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def remove(self, id: str):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)


class Project(BaseAPI):
    class User(BaseAPI):
        def list(self, project_id: str, limit: int = None, offset: str = None):
            params = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(accept="application/json")
            return self.get(url=url, headers=headers, params=params)

    def __init__(self, access_token: str):
        super().__init__(access_token=access_token)
        self.user = self.User(access_token=access_token, endpoint=self._class_name)

    def archive(self, id: str, archive: bool = None):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def create(
        self,
        workspace_id: str,
        name: str,
        description: str = None,
        is_private: bool = None,
    ):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def info(self, id: str):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def list(
        self,
        workspace_id: str,
        disclosure: str = None,
        activity: str = None,
        offset: str = None,
        limit: int = None,
    ):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def tagList(self, id: str, offset: str = None, limit: int = None):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def update(self, id: str, name: str, description: str = None):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)


class Task(BaseAPI):
    def create(
        self,
        project_id: str,
        title: str,
        assign: str = None,
        color: str = None,
        content: str = None,
        end_date: str = None,
        priority: str = None,
        start_date: str = None,
        step: str = None,
        workspace_id: str = None,
    ):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def info(self, id: str):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def list(
        self,
        project_id: str,
        workspace_id: str = None,
        offset: str = None,
        limit: int = None,
    ):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def listByColumn(
        self,
        project_id: str,
        bucket_id: str,
        offset: str = None,
        limit: int = None,
    ):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def move(
        self,
        id: str,
        target_project_id: str,
        target_bucket_id: str = None,
        assign: bool = None,
        follow: bool = None,
    ):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def myTaskList(
        self,
        workspace_id: str,
        offset: str = None,
        limit: int = None,
    ):
        params = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(accept="application/json")
        return self.get(url=url, headers=headers, params=params)

    def remove(self, id: str):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)

    def update(
        self,
        id: str,
        assign: str = None,
        color: str = None,
        content: str = None,
        end_date: str = None,
        priority: str = None,
        start_date: str = None,
        step: str = None,
        title: str = None,
    ):
        data = self.params_to_dict(locals())
        url = self.get_endpoint_url()
        headers = self.get_headers(
            accept="application/json", content_type="application/json"
        )
        return self.post(url=url, headers=headers, data=data)


class Pyswit:
    def __init__(self, access_token: str):
        api_args = {"access_token": access_token}

        self.user = User(**api_args)
        self.workspace = Workspace(**api_args)
        self.message = Message(**api_args)
        self.channel = Channel(**api_args)
        self.project = Project(**api_args)
        self.task = Task(**api_args)


def webhook(url: str, text: str):
    headers = {"Content-Type": "application/json"}
    data = {"text": text}
    r = requests.post(url=url, headers=headers, json=data)
    return json.loads(r.content)
