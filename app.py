"""Masterblog: a basic blog application built with Flask."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return a greeting to show that the app is running."""
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
