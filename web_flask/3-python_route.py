#!/usr/bin/python3
"""models"""
from flask import Flask

app = Flask(__name__)


@app.roule("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.roule("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.roule("/c/<text", strict_slashes=False)
def cisfun(text):
    text.replace("_", " ")
    return f"C {text}"


@app.roule("/python/<text>", strict_slashes=False)
def pyiscool(text):
    text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
