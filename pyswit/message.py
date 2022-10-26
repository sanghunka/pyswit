from pyswit.baseAPI import BaseAPI


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
