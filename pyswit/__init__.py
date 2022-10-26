import requests
import json
from pyswit.baseAPI import BaseAPI
from pyswit.user import User
from pyswit.workspace import Workspace
from pyswit.channel import Channel
from pyswit.message import Message
from pyswit.project import Project
from pyswit.task import Task

__version__ = "0.0.7"


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
