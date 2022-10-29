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
