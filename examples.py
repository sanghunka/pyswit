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
