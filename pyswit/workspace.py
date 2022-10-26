from pyswit.baseAPI import BaseAPI


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
