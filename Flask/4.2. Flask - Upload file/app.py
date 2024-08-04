import os
import bcrypt
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, url_for
from sqlmodel import SQLModel, Field, Session, select, create_engine
from pydantic import BaseModel


app = Flask("Analyze Face")
app.config["UPLOAD_FOLDER"] = "./uploads"
app.config["ALLOWED_EXTENSION"] = {"png", "jpg", "jpeg"}


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



def allowed_file(filename):
    return True


@app.route("/")
def index():
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

        if result and bcrypt.checkpw(login_model.password.encode('utf-8'), result.password.encode('utf-8')):
            print("Welcome, you are logged in")
            return redirect(url_for("upload"))
        else:
            print("Username or password is incorrect")
            return redirect(url_for("login"))


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")

    elif request.method == "POST":
        my_image = request.files["file"]
        if my_image.filename == "":
            return redirect(url_for("upload"))
        else:
            if my_image and allowed_file(my_image.filename):
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                my_image.save(save_path)
                result = DeepFace.analyze(img_path=save_path, actions=["age"])

            return render_template("result.html", age=result[0]["age"])


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

        hashed_password = bcrypt.hashpw(register_data.password.encode('utf-8'), bcrypt.gensalt())

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
                    password=hashed_password.decode('utf-8'),
                    join_time=str(datetime.now()),
                )

                db_session.add(user)
                db_session.commit()
            print("Your register done successfully")
            return redirect(url_for("login"))
        else:
            print("Username already exist, Try another username")
            return redirect(url_for("register"))


@app.route("/bmr", methods=["GET", "POST"])
def bmr():
    if request.method == "GET":
        return render_template("bmr.html")
    elif request.method == "POST":
        gender = request.form["gender"]
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        age = int(request.form["age"])
        if gender == "male":
            result = (10 * weight) + (6.25 * height) - (5 * age) + 5
        elif gender == "female":
            result = (10 * weight) + (6.25 * height) - (5 * age) - 16

        return render_template("resultBMR.html", BMR=result)
