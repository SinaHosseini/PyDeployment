import io
import cv2
import numpy as np
from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI()
friends = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
def read_friends():
    return friends


@app.post("/items")
def add_friend(id: str = Form(), name: str = Form(), age: float = Form()):
    friends[id] = {"name": name, "age": age}
    return friends[id]


@app.delete("/items/{id}")
def remove_friend(id: str):
    if id not in friends:
        raise HTTPException(status_code=404, detail="Item not found")

    del friends[id]
    return {"message": "Item deleted"}


@app.put("/items/{id}")
def update_friend(id: str, name: str = Form(None), age: float = Form(None)):
    if id not in friends:
        raise HTTPException(status_code=404, detail="Item not found")

    if name is not None:
        friends[id]["name"] = name
    if age is not None:
        friends[id]["age"] = age

    return friends[id]


@app.post("/rgb2gray")
async def rgb2gray(inp_file: UploadFile = File(None)):
    if not inp_file.content_type.startswith("image/"):  # type: ignore
        raise HTTPException(status_code=415, detail="Unsupported file type")

    contents = await inp_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image_rgb = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    _, encoded_image = cv2.imencode(".jpg", image_gray)
    image_bytes = encoded_image.tobytes()

    # cv2.imwrite("test.png", image_bytes)
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")
