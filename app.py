"""Masterblog: a basic blog application built with Flask."""
import json
import os

from flask import Flask, redirect, render_template, request, url_for

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


def save_posts(posts):
    """Write the list of blog posts to the JSON storage file."""
    with open(POSTS_FILE, "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


def next_post_id(posts):
    """Return a new unique id: one higher than the highest id in use."""
    return max((post["id"] for post in posts), default=0) + 1


@app.route('/')
def index():
    """Show all blog posts from the JSON file."""
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Show the form for a new post; on POST save the post and go back home."""
    if request.method == 'POST':
        author = request.form.get('author', '').strip()
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if not (author and title and content):
            error = "Please fill in author, title and content."
            return render_template('add.html', error=error, author=author,
                                   title=title, content=content), 400
        blog_posts = load_posts()
        blog_posts.append({
            "id": next_post_id(blog_posts),
            "author": author,
            "title": title,
            "content": content,
        })
        save_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('add.html')



@app.route('/delete/<int:post_id>')
def delete(post_id):
    """Delete the blog post with this id and go back to the home page."""
    blog_posts = load_posts()
    remaining = [post for post in blog_posts if post["id"] != post_id]
    if len(remaining) == len(blog_posts):
        return "Post not found", 404
    save_posts(remaining)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
