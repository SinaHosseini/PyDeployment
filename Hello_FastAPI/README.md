# Pieces Chess♟️
This API show pawn, bishop, knight, rook, queen, and king information ♟️.

Through this API, you can explore and learn about these items, accompanied by images for a visual representation.
The API has been deployed here [pydeployment sqxh.onrender.com](https://pydeployment-sqxh.onrender.com/)

## How to run
```
pip install -r requirements.txt
```

## Getting Started
First you need to run this command in terminal to start the api
```
uvicorn main:app -- reload
```
The base URL of the API endpoints is : 127.0.0.1:8000

**Endpoints**

1) `127.0.0.1:8000/pieces`   
Get a list of all six chess pieces

2) `127.0.0.1:8000/pieces/{pieces_name}` <br>
Get information of a specific piece identified by pieces_name.
Example:
```
127.0.0.1:8000/pieces/king
```


3) `127.0.0.1:8000/pieces/{pieces_name}/image`<br>
Get an image of a specific piece identified by pieces_name.
```
127.0.0.1:8000/pieces/king/image
```
![king_pic](https://github.com/SinaHosseini/PyDeployment/blob/ec50febcf46fa6a0538c257e97079aacac4589b4/Hello_FastAPI/pics/king.png?raw=True)


**All images have been created by fal.ai website**