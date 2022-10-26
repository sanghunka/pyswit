from pyswit.baseAPI import BaseAPI


class User(BaseAPI):
    def info(self):
        return self.get(url=self.get_endpoint_url(), headers=self.get_headers())
