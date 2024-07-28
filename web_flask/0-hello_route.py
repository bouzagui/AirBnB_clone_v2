#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
