from pyswit.baseAPI import BaseAPI


class Project(BaseAPI):
    class User(BaseAPI):
        def list(self, project_id: str, limit: int = None, offset: str = None):
            params = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(accept="application/json")
            return self.get(url=url, headers=headers, params=params)

    class Bucket(BaseAPI):
        def create(self, project_id: str, name: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

        def info(self, id: str, project_id: str):
            params = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(accept="application/json")
            return self.get(url=url, headers=headers, params=params)

        def list(self, project_id: str, limit: int = None, offset: str = None):
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

    def __init__(self, access_token: str):
        super().__init__(access_token=access_token)
        self.user = self.User(access_token=access_token, endpoint=self._class_name)
        self.bucket = self.Bucket(access_token=access_token, endpoint=self._class_name)

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
