#!/usr/bin/python3
"""
First Flask ^^
"""
from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def main():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return f"C {escape(text)}".replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_is_fun(text="is cool"):
    return f"Python {escape(text)}".replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
