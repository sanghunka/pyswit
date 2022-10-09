# 🚧 Under Construction 🚧

Python interface for [swit.io](https://swit.io/)

|                 | HTTP | endpoint                | pyswit                             |                    |
| --------------- | ---- | ----------------------- | ---------------------------------- | ------------------ |
| Users           | GET  | user.info               | swit.user.info()                   | :white_check_mark: |
| Workspaces      |      |                         | [Advanced Only] No plan to support | :x:                |
| Channels        | POST | channel.archive         |                                    |                    |
|                 | POST | channel.create          |                                    |                    |
|                 | POST | channel.createDirect    |                                    |                    |
|                 | GET  | channel.info            |                                    |                    |
|                 | GET  | channel.list            |                                    |                    |
|                 | POST | channel.update          |                                    |                    |
| Messages        | POST | message.comment.create  | swit.message.comment.create()      | :white_check_mark: |
|                 | GET  | message.comment.list    | swit.message.comment.list()        | :white_check_mark: |
|                 | POST | message.comment.remove  | swit.message.comment.remove()      | :white_check_mark: |
|                 | POST | message.create          | swit.message.create()              | :white_check_mark: |
|                 | GET  | message.info            | swit.message.info()                | :white_check_mark: |
|                 | GET  | message.list            | swit.message.list                  | :white_check_mark: |
|                 | POST | message.reaction.create |                                    |                    |
|                 | POST | message.reaction.remove |                                    |                    |
|                 | POST | message.remove          |                                    |                    |
| Ideas           |      |                         |                                    |                    |
| Projects        | POST | project.archive         |                                    |                    |
|                 | POST | project.create          |                                    |                    |
|                 | GET  | project.info            |                                    |                    |
|                 | GET  | project.list            |                                    |                    |
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
|                 | GET  | task.info               |                                    |                    |
|                 | GET  | task.list               |                                    |                    |
|                 | GET  | task.listByColumn       |                                    |                    |
|                 | POST | task.move               |                                    |                    |
|                 | GET  | task.myTaskList         |                                    |                    |
|                 | POST | task.remove             |                                    |                    |
|                 | POST | task.update             |                                    |                    |
| Posts           |      |                         | [Advanced Only] No plan to support | :x:                |
| Boards          |      |                         | [Advanced Only] No plan to support | :x:                |
| Custom fileds   |      |                         |                                    |                    |
| Approvals       |      |                         |                                    |                    |
