import os
import cv2
from flask import Flask, render_template, request, redirect, session, url_for
from deepface import DeepFace


app = Flask("Analyze Face")
app.config["UPLOAD_FOLDER"] = "./uploads"
app.config["ALLOWED_EXTENSION"] = {"png", "jpg", "jpeg"}


def auth(email, password):
    if email == "sina@sina.sina" and password == "1234":
        return True
    else:
        return False


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
        my_email = request.form["email"]
        my_password = request.form["password"]
        result = auth(my_email, my_password)
        if result:
            # upload
            return redirect(url_for("upload"))
        else:
            # login
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


@app.route("/register")
def register():
    return render_template("register.html")


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
