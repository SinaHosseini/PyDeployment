from flask import Flask, render_template, request

app = Flask("Test Project")

@app.route("/", methods=["GET"])
def my_toot():
    name="Sina"
    return render_template("index.html", name=name, x=21)


@app.route("/download", methods=["GET"])
def download():
    media = ["image", "music", "movie"]
    return render_template("download.html", media=media)


@app.route("/me", methods=["GET"])
def my_information():
    my_info = {"firstname": "sina", "email": "sshosseinivaez@gmail.com"}
    return my_info

@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return "This is GET method"
    elif request.method == "POST":
        return "This is POST method"
    