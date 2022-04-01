from flask import Flask, session, render_template, redirect, request, url_for
import os
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


def get_posts():
    path = os.path.join(app.root_path, 'data.json')
    with open(path) as jsonfile:
        data = json.load(jsonfile)
    return data


@app.route("/")
def home():
    return redirect(url_for('posts'))


@app.route("/posts")
def posts():
    posts = get_posts()
    if request.args.get('q'):
        q = request.args.get('q')
        session['q'] = q
        filtered_posts = []
        for item in posts:
            if (q.lower() in item['title'].lower()) or (q.lower() in item['description'].lower()):
                filtered_posts.append(item)
        return render_template('posts.html', posts=filtered_posts, q=q)
    session['q'] = None
    return render_template('posts.html', posts=posts)


@app.route("/post/<int:id>")
def post(id):
    posts = get_posts()
    q = session['q']
    for post in posts:
        if post['post_id'] == id:
            # return render_template("post.html", post=post)
            return render_template("post.html", post=post, q=q)
    return render_template("post.html")
