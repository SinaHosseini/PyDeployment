import requests
import os
import dotenv


dotenv = dotenv.load_dotenv()

API_key = os.getenv("Planet_API_key")
url = "https://my-api.plantnet.org/v2/identify/all"

headers = {
}

payload = {
    "api-key": API_key
}

files = {
    "images": open("plant.jpg", "rb")
}
response = requests.post(url, headers=headers, params=payload, files=files)
print(response.status_code)
print(response.json())
