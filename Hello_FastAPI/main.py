import io
import cv2
from fastapi import FastAPI ,HTTPException, status
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/")
def introducing():
    return "This API show pawn, bishop, knight, rook, queen, and king information ♟️"

@app.get("/pieces")
def pieces():
    return "pawn ♙, ♟  bishop ♗, ♝  knight ♘, ♞  rook  ♖, ♜ queen ♕, ♛  king ♔, ♚"

@app.get("/pieces/{pieces_name}")
def pieces_name(pieces_name: str):
    if pieces_name == "pawn":
        return "The pawn (♙, ♟) is the most numerous and weakest piece in the game of chess. It may move one square directly forward, it may move two squares directly forward on its first move, and it may capture one square diagonally forward."
    elif pieces_name == "bishop":
        return "The bishop (♗, ♝) is a piece in the game of chess. It moves and captures along diagonals without jumping over intervening pieces. Each player begins the game with two bishops. The starting squares are c1 and f1 for White's bishops, and c8 and f8 for Black's bishops."
    elif pieces_name == "knight":
        return "The knight (♘, ♞) is a piece in the game of chess, represented by a horse's head and neck. It moves two squares vertically and one square horizontally, or two squares horizontally and one square vertically, jumping over other pieces. Each player starts the game with two knights on the b- and g-files, each located between a rook and a bishop."
    elif pieces_name == "rook":
        return "The rook (♖, ♜) is a piece in the game of chess. It may move any number of squares horizontally or vertically without jumping, and it may capture an enemy piece on its path; additionally, it may participate in castling. Each player starts the game with two rooks, one in each corner on their own side of the board."
    elif pieces_name == "queen":
        return "The queen (♕, ♛) is the most powerful piece in the game of chess. It can move any number of squares vertically, horizontally or diagonally, combining the powers of the rook and bishop. Each player starts the game with one queen, placed in the middle of the first rank next to the king. Because the queen is the strongest piece, a pawn is promoted to a queen in the vast majority of cases."
    elif pieces_name == "king":
        return "The king (♔, ♚) is the most important piece in the game of chess. It may move to any adjoining square; it may also perform, in tandem with the rook, a special move called castling. If a player's king is threatened with capture, it is said to be in check, and the player must remove the threat of capture immediately. If this cannot be done, the king is said to be in checkmate, resulting in a loss for that player. A player cannot make any move that places their own king in check. Despite this, the king can become a strong offensive piece in the endgame or, rarely, the middlegame."
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="please enter correct pieces chess")
    

@app.get("/pieces/{pieces_name}/image")
def images(pieces_name):
    if pieces_name == "pawn":
        image = cv2.imread("pics\pawn.png") 
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")
    elif pieces_name == "bishop":
        image = cv2.imread("pics\bishop.png")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")
    elif pieces_name == "knight":
        image = cv2.imread("pics\horse.png") # type: ignore
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")
    elif pieces_name == "rook":
        image = cv2.imread("pics\rook.png")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")
    elif pieces_name == "queen":
        image = cv2.imread("pics\queen.png") # type: ignore
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")
    elif pieces_name == "king":
        image = cv2.imread("pics\king.png") # type: ignore
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="please enter correct pieces chess")
    
