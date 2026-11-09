# Masterblog

A basic blog application built with Flask (Masterschool exercise). Blog posts are stored in
`blog_posts.json`; every post has an `id`, `author`, `title`, `content` and `likes`.

## Run

```
pip3 install -r requirements.txt
python3 app.py
```

Then open http://localhost:5000.

## Routes

| Route | Methods | What it does |
|---|---|---|
| `/` | GET | Lists all blog posts |
| `/add` | GET, POST | Form for a new post; POST saves it and redirects home |
| `/update/<post_id>` | GET, POST | Form prefilled with the post; POST saves the changes |
| `/delete/<post_id>` | GET | Deletes the post and redirects home |
| `/like/<post_id>` | GET | Adds one like and redirects home (bonus) |

Unknown post ids return 404; empty form fields return the form with an error (400).
