# Pyswit: Python + Swit.io

Python interface for [swit.io](https://swit.io/)

[![PyPI version fury.io](https://badge.fury.io/py/pyswit.svg)](https://pypi.org/project/pyswit/)
[![PyPI format](https://img.shields.io/pypi/format/pyswit.svg)](https://pypi.python.org/pypi/pyswit/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyswit.svg)](https://pypi.python.org/pypi/pyswit/)
[![PyPI license](https://img.shields.io/pypi/l/pyswit.svg)](https://pypi.python.org/pypi/pyswit/)

<br>

## Requirements

This library requires Python 3.6 or later.

## Installation

```sh
$ pip install pyswit
```

## Examples

```py
from pyswit import Pyswit

# How to get access token: https://developers.swit.io/documentation#authentication
access_token = "<your access token>"
swit = Pyswit(access_token)

# User
print(swit.user.info())

# Create a message
channel_id = "<your_channel_id>"  # not channel name
response = swit.message.create(channel_id=channel_id, content="Hello World")

# Get message_id
message_id = response["data"]["message"]["message_id"]

# React to a message
swit.message.reaction.create(message_id=message_id, reaction_name=":smile:")

# Comment on a message
swit.message.comment.create(message_id=message_id, content="Comment string here")
```

## Documentation

[Swit.io Developer documentation](https://developers.swit.io/documentation#introduction)

Currently, Pyswit supports the following API.

|                 | HTTP | endpoint                | pyswit                             |                    |
| --------------- | ---- | ----------------------- | ---------------------------------- | ------------------ |
| Users           | GET  | user.info               | swit.user.info()                   | :white_check_mark: |
| Workspaces      |      |                         | [Advanced Only] No plan to support | :x:                |
| Channels        | POST | channel.archive         |                                    |                    |
|                 | POST | channel.create          |                                    |                    |
|                 | POST | channel.createDirect    |                                    |                    |
|                 | GET  | channel.info            |                                    |                    |
|                 | GET  | channel.list            | swit.channel.list()                | :white_check_mark: |
|                 | POST | channel.update          |                                    |                    |
| Messages        | POST | message.comment.create  | swit.message.comment.create()      | :white_check_mark: |
|                 | GET  | message.comment.list    | swit.message.comment.list()        | :white_check_mark: |
|                 | POST | message.comment.remove  | swit.message.comment.remove()      | :white_check_mark: |
|                 | POST | message.create          | swit.message.create()              | :white_check_mark: |
|                 | GET  | message.info            | swit.message.info()                | :white_check_mark: |
|                 | GET  | message.list            | swit.message.list()                | :white_check_mark: |
|                 | POST | message.reaction.create | swit.message.reaction.create()     | :white_check_mark: |
|                 | POST | message.reaction.remove | swit.message.reaction.remove()     | :white_check_mark: |
|                 | POST | message.remove          | swit.message.remove()              | :white_check_mark: |
| Ideas           |      |                         |                                    |                    |
| Projects        | POST | project.archive         |                                    |                    |
|                 | POST | project.create          |                                    |                    |
|                 | GET  | project.info            |                                    |                    |
|                 | GET  | project.list            | swit.project.list()                | :white_check_mark: |
|                 | GET  | project.tagList         |                                    |                    |
|                 | POST | project.update          |                                    |                    |
|                 | GET  | project.user.list       |                                    |                    |
| Project buckets |      |                         |                                    |                    |
| Tasks           | POST | task.assignee.add       |                                    |                    |
|                 | POST | task.asignee.remove     |                                    |                    |
|                 | POST | task.checklist.create   |                                    |                    |
|                 | GET  | task.checklist.info     |                                    |                    |
|                 | GET  | task.checklist.list     |                                    |                    |
|                 | POST | task.checklist.remove   |                                    |                    |
|                 | POST | task.checklist.update   |                                    |                    |
|                 | POST | task.comment.create     |                                    |                    |
|                 | GET  | task.comment.list       |                                    |                    |
|                 | POST | task.comment.remove     |                                    |                    |
|                 | POST | task.comment.update     |                                    |                    |
|                 | POST | task.create             |                                    |                    |
|                 | POST | task.follow.add         |                                    |                    |
|                 | POST | task.follow.remove      |                                    |                    |
|                 | GET  | task.info               | swit.task.info()                   | :white_check_mark: |
|                 | GET  | task.list               | swit.task.list()                   | :white_check_mark: |
|                 | GET  | task.listByColumn       | swit.task.listByColumn()           | :white_check_mark: |
|                 | POST | task.move               | swit.task.move()                   | :white_check_mark: |
|                 | GET  | task.myTaskList         | swit.task.myTaskList()             | :white_check_mark: |
|                 | POST | task.remove             | swit.task.remove()                 | :white_check_mark: |
|                 | POST | task.update             | swit.task.update()                 | :white_check_mark: |
| Posts           |      |                         | [Advanced Only] No plan to support | :x:                |
| Boards          |      |                         | [Advanced Only] No plan to support | :x:                |
| Custom fileds   |      |                         |                                    |                    |
| Approvals       |      |                         |                                    |                    |
