# from flask import Flask, render_template
# import requests
#
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
#     response = requests.get(blog_url)
#     all_posts = response.json()
#     return render_template("index.html", posts=all_posts)
#
# @app.route('/post/<num>')
# def get_blog(num):
#     blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
#     response = requests.get(blog_url)
#     all_posts = response.json()
#     return render_template("post.html", posts=all_posts)
#
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

# Fetch all blog posts once
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_data = response.json()

# Create a list of Post objects
all_posts = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in blog_data]


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def get_blog(num):
    requested_post = next((post for post in all_posts if post.id == num), None)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
