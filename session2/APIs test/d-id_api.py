import requests
import json
import os
import dotenv

url = "https://api.d-id.com/clips"

payload = {
    "script": {
        "type": "text",
        "subtitles": "false",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "ssml": "false"
    },
    "config": {"result_format": "mp4"},
    "presenter_config": {"crop": {"type": "rectangle"}}
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "key"
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.text)
