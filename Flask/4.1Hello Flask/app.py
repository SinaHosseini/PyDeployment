from flask import Flask, request, render_template

app = Flask("My Personal WebSite")


@app.route("/")
def my_root():
    return render_template("index.html")


@app.route("/login.html")
def login():
    return render_template("login.html")
