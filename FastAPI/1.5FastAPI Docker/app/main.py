import sqlite3
from fastapi import FastAPI, Form, HTTPException

app = FastAPI()


def database():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()

    return con, cur


@app.get("/")
def read_root():
    return "Hi, welcome to my api In this api there is  requests for read, add, update and remove database--created by Sina Hosseini"


@app.get("/items")
def read_data():
    _, cur = database()
    res = cur.execute("SELECT * FROM tasks")
    res = res.fetchall()

    return res


@app.post("/items")
def add_data(id: int = Form(), tittle: str = Form(), description: str = Form(), time: str = Form(), status: int = Form(0)):
    con, cur = database()
    cur.execute(
        f"INSERT INTO tasks (id, tittle, description, time, status) VALUES (?, ?, ?, ?, ?)",
        (id, tittle, description, time, status)
    )
    con.commit()

    return read_data()


@app.put("/items/{id}")
def update_data(id: int, tittle: str = Form(), description: str = Form(), time: str = Form(), status: int = Form()):
    con, cur = database()
    cur.execute("SELECT id FROM tasks")
    exs_id = [row[0] for row in cur.fetchall()]
    if id not in exs_id:
        raise HTTPException(status_code=404, detail="Item not found")

    else:
        cur.execute("UPDATE tasks SET tittle=?, description=?, time=?, status=? WHERE id=?",
                    (tittle, description, time, status, id))
        con.commit()

    return read_data()


@app.delete("/items/{id}")
def delete_item(id: int):
    con, cur = database()
    cur.execute("SELECT id FROM tasks")
    exs_id = [row[0] for row in cur.fetchall()]
    if id not in exs_id:
        raise HTTPException(status_code=404, detail="Item not found")

    else:
        cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        con.commit()
        return {"message": "Item deleted"}