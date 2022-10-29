from pyswit.baseAPI import BaseAPI


class Task(BaseAPI):
    class Assignee(BaseAPI):
        def add(self, task_id: str, user_id: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

        def remove(self, task_id: str, user_id: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

    class Checklist(BaseAPI):
        def create(self, task_id: str, content: str):
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

        def list(self, task_id: str, limit: int = None, offset: str = None):
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

        def update(self, id: str, content: str, is_complete: bool = None):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

    class Comment(BaseAPI):
        def create(self, task_id: str, content: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

        def list(self, task_id: str, limit: int = None, offset: str = None):
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

        def update(self, id: str, content: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

    class Follow(BaseAPI):
        def add(self, task_id: str, user_id: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

        def remove(self, task_id: str, user_id: str):
            data = self.params_to_dict(locals())
            url = self.get_endpoint_url()
            headers = self.get_headers(
                accept="application/json", content_type="application/json"
            )
            return self.post(url=url, headers=headers, data=data)

    def __init__(self, access_token: str):
        super().__init__(access_token=access_token)
        self.assignee = self.Assignee(
            access_token=access_token, endpoint=self._class_name
        )
        self.checklist = self.Checklist(
            access_token=access_token, endpoint=self._class_name
        )
        self.comment = self.Comment(
            access_token=access_token, endpoint=self._class_name
        )
        self.follow = self.Follow(access_token=access_token, endpoint=self._class_name)

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
