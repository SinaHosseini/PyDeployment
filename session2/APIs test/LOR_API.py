import requests
import json
import os
import dotenv

dotenv = dotenv.load_dotenv()

LOR_API_key = os.getenv("LOR_API_key")
headers = {"Authorization": LOR_API_key}

response = requests.get("https://the-one-api.dev/v2/movie", headers=headers)
print(response.status_code)
print(json.loads(response.text))
