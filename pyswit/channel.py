from pyswit.baseAPI import BaseAPI


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
