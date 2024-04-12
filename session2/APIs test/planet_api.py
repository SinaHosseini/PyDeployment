import requests
import json
import os
import dotenv


dotenv = dotenv.load_dotenv()

Planet_API_key = os.getenv("Planet_API_key")
url = "https://my-api.plantnet.org/v2/identify/all"

headers = {
}

payload = {
    "api-key": Planet_API_key
}

files = {
    "images": open("...", "rb")
}
response = requests.post(url, headers=headers, params=payload, files=files)
