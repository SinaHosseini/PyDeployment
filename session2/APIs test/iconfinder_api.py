import requests
import json
import os
import dotenv

dotenv = dotenv.load_dotenv()

IconFinder_API_key = os.getenv("IconFinder_API_key")


url = "https://api.iconfinder.com/v4/icons/search?query=arrow&count=10"

headers = {
    "accept": "application/json",
    "Authorization": IconFinder_API_key
}
response = requests.get(url, headers=headers)
print(response.status_code)
print(json.loads(response.text))
