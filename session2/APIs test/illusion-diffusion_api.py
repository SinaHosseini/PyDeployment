import requests
import json
import os
import dotenv

dotenv = dotenv.load_dotenv()

IllusionDiffusion_API_key = os.getenv("IllusionDiffusion_API_key")
url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"

headers = {
    "Authorization": IllusionDiffusion_API_key,
    "Content-Type": "application/json"
}

payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
    "prompt": "(masterpiece:1.4), (best quality), (detailed), landscape, Rainy forest of northern Canada",
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(json.loads(response.text))
