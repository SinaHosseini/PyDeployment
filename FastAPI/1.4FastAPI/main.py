import cv2
import numpy as np
from deepface import DeepFace
from fastapi import FastAPI, File, UploadFile, HTTPException

# objs = DeepFace.analyze(img_path = "photo_2024-05-03_20-40-35.jpg",
#         actions = ['age', 'gender', 'race', 'emotion']
# )
# for obj in objs:
#     print("Age:", obj["age"])
#     print("Gender:", obj["dominant_gender"])
#     print("Race:", obj["dominant_race"])
#     print("Emotion:", obj["dominant_emotion"])

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello, welcome to my api In this api there is face analysis is done, such as age, gender, race and emotion, just send a photo file and see the result--created by Sina Hosseini"


@app.post("/analyze_image")
async def image_processing(inp_file: UploadFile = File(None)):
    if not inp_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported file type")
    contents = await inp_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image_path = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    cv2.imwrite("img.jpg", image_path)

    objs = DeepFace.analyze(img_path="img.jpg", actions=[
                            "age", "gender", "race", "emotion"])
    for obj in objs:
        age = obj["age"]
        gender = obj["dominant_gender"]
        race = obj["dominant_race"]
        emotion = obj["dominant_emotion"]

    return age, gender, race, emotion
