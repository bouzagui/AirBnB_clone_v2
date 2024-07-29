#!/usr/bin/python3
"""model doc"""
from flask import Flask, render_tamplate
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def statelist():
    all_states = storage.all(State)
    return render_tamplate("7-states_list.html", all_states=all_states)


def close(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
