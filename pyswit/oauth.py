from pyswit.baseAPI import BaseAPI


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
        if scope:
            self.scope = self._get_scope(scope)
        else:
            self.scope = None

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
            f"&scope={self.scope}"
        )

        if self.state:
            url = url + f"&state={self.state}"

        print()
        print(f"🔗 {url}")
        print()
        print("This URL will be redirected to the authentication web page.")
        print("Please accept the permission request.")
        print()
        if (self.state == "") | (self.state is None):
            print(f"🔗 {self.redirect_uri}?code=<your-code>")
        else:
            print(f"🔗 {self.redirect_uri}?code=<your-code>&state={self.state}")
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
