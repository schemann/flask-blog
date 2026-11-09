"""Masterblog: a basic blog application built with Flask."""
import json
import os

from flask import Flask, render_template

app = Flask(__name__)

# The JSON file next to app.py is the storage for all blog posts.
POSTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog_posts.json")


def load_posts():
    """Return the list of blog posts from the JSON storage file."""
    try:
        with open(POSTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


@app.route('/')
def index():
    """Show all blog posts from the JSON file."""
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
