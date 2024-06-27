import requests
import json
import os
import dotenv


# headers = {"Authorization": "Bearer zScMmwnrFYT-X8dUvZ8w"}
#
# response = requests.get("https://the-one-api.dev/v2/movie", headers=headers)
# print(response.status_code)
# print(json.loads(response.text))

# -----------------------------------------------------------------------------

# url = "https://api.iconfinder.com/v4/icons/search?query=arrow&count=10"
#
# headers = {
# "accept": "application/json",
# "Authorization": "Bearer yCP1vVXe40SXzAOvF3brpSZHMVx0JGY6qVaqk69Ek6l1yABspUqL1qHUNc6f77Zr"
# }
# response = requests.get(url, headers=headers)
# print(response.status_code)
# print(json.loads(response.text))

# ----------------------------------------------------------------------------

# url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
#
# headers = {
# "Authorization": "Key d8a1e9bc-05e7-4333-9d6e-e290df6f50d4:1d7ce88cf10b7f7d63f984a8793a9bd8",
# "Content-Type": "application/json"
# }
#
# payload = {
# "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
# "prompt": "(masterpiece:1.4), (best quality), (detailed), landscape, Rainy forest of northern Canada",
# "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime"
# }
#
# response = requests.post(url, headers=headers, json=payload)
# print(response.status_code)
# print(json.loads(response.text))

# -------------------------------------------------------------------------------

# url = "https://api.d-id.com/clips"
#
# payload = {
# "script": {
# "type": "text",
# "subtitles": "false",
# "provider": {
# "type": "microsoft",
# "voice_id": "en-US-JennyNeural"
# },
# "ssml": "false"
# },
# "config": { "result_format": "mp4" },
# "presenter_config": { "crop": { "type": "rectangle" } }
# }
# headers = {
# "accept": "application/json",
# "content-type": "application/json",
# "Authorization": "key"
# }
#
# response = requests.post(url, json=payload, headers=headers)
# print(response.status_code)
# print(response.text)

# ---------------------------------------------------------------------------------

# url = "https://my-api.plantnet.org/v2/identify/all"
#
# headers = {
# }
#
# payload = {
# "api-key": "2b10AYoq78Yz0gVVJw2mIRe4"
# }
#
# files = {
# "images": open("...", "rb")
# }
# response = requests.post(url, headers=headers, params=payload, files=files)

# ----------------------------------------------------------------------------

from fastapi import FastAPI

app = FastAPI()


@app.get("/sina")
def read_root():
    return {"Hello": "World"}




