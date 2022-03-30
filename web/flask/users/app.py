from flask import Flask
from flask import request
from flask import render_template
import csv
import os

app = Flask(__name__)


def get_users():
    all_users = {}
    path = os.path.join(app.root_path, 'MOCK_DATA.csv')
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for id, name in reader:
            all_users[id] = name
    return all_users


@app.route("/")
def home():
    return "Hello world!!!"


@app.route("/users")
def users():
    all_users = get_users()
    if request.args.get('q'):
        q = request.args.get('q')
        filtered_users = {}
        for id, email in all_users.items():
            if q in email:
                filtered_users[id] = email
        return render_template('users.html', users=filtered_users, q=q)
    return render_template('users.html', users=all_users)


@app.route("/user/<int:id>")
def user(id):
    users = get_users()
    email = users[str(id)]
    # email = users.get(id)
    return render_template('user.html', id=id, email=email)

