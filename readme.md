# Pyswit: Python + Swit.io

Python interface for [Swit.io](https://swit.io/) RESTful API

[![PyPI](https://img.shields.io/pypi/v/pyswit?color=green)](https://pypi.python.org/pypi/pyswit/)
[![PyPI download month](https://img.shields.io/pypi/dm/pyswit.svg)](https://pypi.python.org/pypi/pyswit/)
[![PyPI format](https://img.shields.io/pypi/format/pyswit.svg)](https://pypi.python.org/pypi/pyswit/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyswit.svg)](https://pypi.python.org/pypi/pyswit/)
[![PyPI license](https://img.shields.io/pypi/l/pyswit?color=%23D22128)](https://pypi.python.org/pypi/pyswit/)

<br>

## Requirements

This library requires Python 3.6 or later.

## Installation

```sh
$ pip install pyswit
```

## Authentication

- You need `access token` to use Swit Open API.
- Please refer [Getting started with authentication](./docs/getting-started-with-authentication.md)

## Examples

```py
from pyswit import Pyswit

access_token = "<your access token>"
swit = Pyswit(access_token)

# User
print(swit.user.info())

# Create a message
channel_id = "<your_channel_id>"  # not channel name
response = swit.message.create(channel_id=channel_id, content="Hello, World!")

# Get message_id
message_id = response["data"]["message"]["message_id"]

# React to a message
swit.message.reaction.create(message_id=message_id, reaction_name=":smile:")

# Comment on a message
swit.message.comment.create(message_id=message_id, content="Comment string here")
```

## Webhook

Pyswit supports webhook.

Webhook API does not require access token

```sh
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' <your_webhook_url>
```

The above curl request can be implemented with pyswit as follows.

```py
from pyswit.webhook import webhook

webhook_url="<your_webhook_url>"
webhook(url=webhook_url, text="Hello, World!")
```

## Documentation

[Swit.io Developer documentation](https://developers.swit.io/documentation#introduction)

- Currently, Pyswit supports the following API.

|                 | HTTP | endpoint                | pyswit             |
| --------------- | ---- | ----------------------- | ------------------ |
| Users           | GET  | user.info               | :white_check_mark: |
| Workspaces      | GET  | workspace.info          | :white_check_mark: |
|                 | GET  | workspace.list          | :white_check_mark: |
|                 | POST | workspace.update        | :white_check_mark: |
|                 | GET  | workspace.user.info     | :white_check_mark: |
|                 | GET  | workspace.user.list     | :white_check_mark: |
|                 | POST | workspace.user.update   | :white_check_mark: |
| Channels        | POST | channel.archive         | :white_check_mark: |
|                 | POST | channel.create          | :white_check_mark: |
|                 | POST | channel.createDirect    | :white_check_mark: |
|                 | GET  | channel.info            | :white_check_mark: |
|                 | GET  | channel.list            | :white_check_mark: |
|                 | POST | channel.update          | :white_check_mark: |
| Messages        | POST | message.comment.create  | :white_check_mark: |
|                 | GET  | message.comment.list    | :white_check_mark: |
|                 | POST | message.comment.remove  | :white_check_mark: |
|                 | POST | message.create          | :white_check_mark: |
|                 | GET  | message.info            | :white_check_mark: |
|                 | GET  | message.list            | :white_check_mark: |
|                 | POST | message.reaction.create | :white_check_mark: |
|                 | POST | message.reaction.remove | :white_check_mark: |
|                 | POST | message.remove          | :white_check_mark: |
| Ideas           | POST | idea.comment.create     | :white_check_mark: |
|                 | GET  | idea.comment.list       | :white_check_mark: |
|                 | POST | idea.comment.remove     | :white_check_mark: |
|                 | POST | idea.create             | :white_check_mark: |
|                 | GET  | idea.info               | :white_check_mark: |
|                 | GET  | idea.list               | :white_check_mark: |
|                 | POST | idea.remove             | :white_check_mark: |
|                 | POST | idea.reaction.create    | :white_check_mark: |
|                 | POST | idea.reaction.remove    | :white_check_mark: |
| Projects        | POST | project.archive         | :white_check_mark: |
|                 | POST | project.create          | :white_check_mark: |
|                 | GET  | project.info            | :white_check_mark: |
|                 | GET  | project.list            | :white_check_mark: |
|                 | GET  | project.tagList         | :white_check_mark: |
|                 | POST | project.update          | :white_check_mark: |
|                 | GET  | project.user.list       | :white_check_mark: |
| Project buckets | POST | project.bucket.create   | :white_check_mark: |
|                 | GET  | project.bucket.info     | :white_check_mark: |
|                 | GET  | project.bucket.list     | :white_check_mark: |
|                 | POST | project.bucket.update   | :white_check_mark: |
| Tasks           | POST | task.assignee.add       | :white_check_mark: |
|                 | POST | task.asignee.remove     | :white_check_mark: |
|                 | POST | task.checklist.create   | :white_check_mark: |
|                 | GET  | task.checklist.info     | :white_check_mark: |
|                 | GET  | task.checklist.list     | :white_check_mark: |
|                 | POST | task.checklist.remove   | :white_check_mark: |
|                 | POST | task.checklist.update   | :white_check_mark: |
|                 | POST | task.comment.create     | :white_check_mark: |
|                 | GET  | task.comment.list       | :white_check_mark: |
|                 | POST | task.comment.remove     | :white_check_mark: |
|                 | POST | task.comment.update     | :white_check_mark: |
|                 | POST | task.create             | :white_check_mark: |
|                 | POST | task.follow.add         | :white_check_mark: |
|                 | POST | task.follow.remove      | :white_check_mark: |
|                 | GET  | task.info               | :white_check_mark: |
|                 | GET  | task.list               | :white_check_mark: |
|                 | GET  | task.listByColumn       | :white_check_mark: |
|                 | POST | task.move               | :white_check_mark: |
|                 | GET  | task.myTaskList         | :white_check_mark: |
|                 | POST | task.remove             | :white_check_mark: |
|                 | POST | task.update             | :white_check_mark: |
| Posts           |      |                         | :x:                |
| Boards          |      |                         | :x:                |
| Custom fileds   |      |                         | :x:                |
| Approvals       |      |                         | :x:                |

- Advanced Only API: `Posts`, `Boards`, `Custom fileds`, `Approvals`
- Pyswit has no plan to support Advanced Only API
