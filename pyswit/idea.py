from pyswit.baseAPI import BaseAPI


class Idea(BaseAPI):
    class Comment(BaseAPI):
        pass

    class Reaction(BaseAPI):
        pass

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

