import os
from datetime import datetime
import bcrypt
from flask import Flask, render_template, request, redirect, session, url_for
from sqlmodel import SQLModel, Field, Session, select, create_engine
from pydantic import BaseModel


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str = Field()
    last_name: str = Field()
    email: str = Field()
    username: str = Field()
    age: int = Field()
    country: str = Field()
    city: str = Field()
    password: str = Field()
    join_time: str = Field()


engine = create_engine("sqlite:///./database.db", echo=True)
SQLModel.metadata.create_all(engine)


class RegisterModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    age: int
    country: str
    city: str
    password: str
    confirm_password: str
    join_time: str


class LoginModel(BaseModel):
    username: str
    password: str


app = Flask("My Personal WebSite")


@app.route("/")
def my_root():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        try:
            login_model = LoginModel(
                username=request.form["username"], password=request.form["password"]
            )
        except:
            print("Type error")
            return redirect(url_for("login"))

        with Session(engine) as db_session:
            statement = select(User).where(User.username == login_model.username)
            result = db_session.exec(statement).first()

        if result and bcrypt.checkpw(
            login_model.password.encode("utf-8"), result.password.encode("utf-8")
        ):
            print("Welcome, you are logged in")
            return render_template("index.html")
        else:
            print("Username or password is incorrect")
            return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        try:
            register_data = RegisterModel(
                first_name=request.form["first_name"],
                last_name=request.form["last_name"],
                email=request.form["email"],
                username=request.form["username"],
                age=request.form["age"],
                country=request.form["country"],
                city=request.form["city"],
                password=request.form["password"],
                confirm_password=request.form["confirm_password"],
                join_time=str(datetime.now()),
            )
        except:
            print("type error")
            return redirect(url_for("register"))

        if register_data.password != register_data.confirm_password:
            print("Passwords do not match")
            return redirect(url_for("register"))

        hashed_password = bcrypt.hashpw(
            register_data.password.encode("utf-8"), bcrypt.gensalt()
        )

        with Session(engine) as db_session:
            statement = select(User).where(User.username == register_data.username)
            result = db_session.exec(statement).first()

        if not result:
            with Session(engine) as db_session:
                user = User(
                    first_name=register_data.first_name,
                    last_name=register_data.last_name,
                    email=register_data.email,
                    username=register_data.username,
                    age=register_data.age,
                    country=register_data.country,
                    city=register_data.city,
                    password=hashed_password.decode("utf-8"),
                    join_time=str(datetime.now()),
                )

                db_session.add(user)
                db_session.commit()
            print("Your register done successfully")
            return redirect(url_for("login"))
        else:
            print("Username already exist, Try another username")
            return redirect(url_for("register"))
