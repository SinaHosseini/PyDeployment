import requests
import os
import dotenv
import argparse
from urllib.request import urlretrieve


def make_img():
    parser = argparse.ArgumentParser(
        description="a code that takes text from the user and turns it into a picture")
    parser.add_argument("--message", type=str, help="enter yout text")

    args = parser.parse_args()

    user_text = f'{args.message}'
    print(user_text)

    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"

    headers = {
        "Authorization": IllusionDiffusion_API_key,
        "Content-Type": "application/json"
    }

    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        f"prompt": "(masterpiece:1.4), (best quality), (detailed),"+user_text,
        "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)
    image_response = response.json()["image"]["url"]
    return image_response


def identification_plant():

    response = make_img()
    urlretrieve(response, "plant.jpg")

    url = "https://my-api.plantnet.org/v2/identify/all"

    headers = {
    }

    payload = {
        "api-key": Planet_API_key
    }

    files = {
        "images": open("plant.jpg", "rb")
    }
    response = requests.post(url, headers=headers, params=payload, files=files)
    print(response.status_code)
    answer = response.json()["results"]
    answer = answer.pop(4)
    answer = answer["species"]
    return answer


if __name__ == '__main__':

    dotenv = dotenv.load_dotenv()

    Planet_API_key = os.getenv("Planet_API_key")
    IllusionDiffusion_API_key = os.getenv("IllusionDiffusion_API_key")
    name = identification_plant()
    name = name["commonNames"][0]
    print(name)
