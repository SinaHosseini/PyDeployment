from fastapi import FastAPI

app = FastAPI()


@app.get("/sina")
def read_root():
    return {"Hello": "World"}