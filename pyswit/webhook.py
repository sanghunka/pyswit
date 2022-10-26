import requests
import json


def webhook(url: str, text: str):
    headers = {"Content-Type": "application/json"}
    data = {"text": text}
    r = requests.post(url=url, headers=headers, json=data)
    return json.loads(r.content)
