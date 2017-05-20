from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/data/<year>/<month>')
def data(year, month):
    with open("./data/{}-{}.txt".format(year, month), "r") as file:
        return str(file.readlines())
