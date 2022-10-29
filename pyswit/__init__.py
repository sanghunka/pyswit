from pyswit.user import User
from pyswit.workspace import Workspace
from pyswit.channel import Channel
from pyswit.message import Message
from pyswit.idea import Idea
from pyswit.project import Project
from pyswit.task import Task

__version__ = "1.0.0"


class Pyswit:
    def __init__(self, access_token: str):
        api_args = {"access_token": access_token}

        self.user = User(**api_args)
        self.workspace = Workspace(**api_args)
        self.channel = Channel(**api_args)
        self.message = Message(**api_args)
        self.idea = Idea(**api_args)
        self.project = Project(**api_args)
        self.task = Task(**api_args)
