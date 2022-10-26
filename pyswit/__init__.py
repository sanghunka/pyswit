import requests
import json
from pyswit.baseAPI import BaseAPI
from pyswit.user import User
from pyswit.workspace import Workspace
from pyswit.channel import Channel


__version__ = "0.0.7"


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


class Oauth(BaseAPI):
    def __init__(
        self,
        access_token: str = None,
        refresh_token: str = None,
        client_id: str = None,
        client_secret: str = None,
        redirect_uri: str = None,
        response_type: str = None,
        state: str = None,
        scope: str = None,
    ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.state = state
        self.scope = self._get_scope(scope)

    def _get_scope(self, scope_type):
        free_standard_scopes = [
            "channel:read",
            "channel:write",
            "idea:read",
            "idea:write",
            "message:read",
            "message:write",
            "project:read",
            "project:write",
            "task:read",
            "task:write",
            "user:read",
            "workspace:read",
            "workspace:write",
            "approval:read",
            "approval:write",
        ]

        scope_type = scope_type.lower()
        if scope_type == "free":
            return "+".join(free_standard_scopes)
        elif scope_type == "standard":
            return "+".join(free_standard_scopes)
        elif scope_type == "advanced":
            advanced_scopes = free_standard_scopes + ["admin:read", "admin:write"]
            return "+".join(advanced_scopes)
        else:
            return scope_type

    def authorize_helper(self):
        self.client_id = input("client_id? ")
        self.redirect_uri = input("redirect_uri? ")
        self.response_type = input(
            "response_type? [Currently, only 'code' is supported] "
        )
        self.state = input("state? ")
        self.scope = self._get_scope(input("scope? [free/standard/advanced/custom] "))

    def authorize(self):
        endpoint_url = "https://openapi.swit.io/oauth/authorize"

        url = (
            f"{endpoint_url}?client_id={self.client_id}"
            f"&redirect_uri={self.redirect_uri}"
            f"&response_type={self.response_type}"
            f"&state={self.state}"
            f"&scope={self.scope}"
        )

        print()
        print(f"🔗 {url}")
        print()
        print("This URL will be redirected to the authentication web page.")
        print("Please accept the permission request.")
        print()
        if self.state != "":
            print(f"🔗 {self.redirect_uri}?code=<your-code>&state={self.state}")
        else:
            print(f"🔗 {self.redirect_uri}?code=<your-code>")
        print()
        print("Upon confirmation, the user is redirected to this url.")
        print(
            "In the query string, <your-code> is authorization code which will be used to exchange for an access token."
        )

    def exchange_for_access_token(self, code: str):
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "code": code,
        }
        url = "https://openapi.swit.io/oauth/token"
        headers = self.get_headers(
            content_type="application/x-www-form-urlencoded", authorization=False
        )
        try:
            res = self.post(url=url, headers=headers, data=data)
            self.access_token = res["access_token"]
            self.refresh_token = res["refresh_token"]
        except:
            return res
        return res

    def refresh_access_token(self, refresh_token: str = None):
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
        }
        url = "https://openapi.swit.io/oauth/token"
        headers = self.get_headers(
            content_type="application/x-www-form-urlencoded", authorization=False
        )
        try:
            res = self.post(url=url, headers=headers, data=data)
            self.access_token = res["access_token"]
            self.refresh_token = res["refresh_token"]
        except:
            return res
        return res


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
