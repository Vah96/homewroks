from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

posts = [{
    "id": 1,
    'title': 'Example of title',
    'text': 'Description of title'
},{
    "id": 2,
    'title': 'Example of title',
    'text': 'Description of title'
},{
    "id": 3,
    'title': 'Example of title',
    'text': 'Description of title'
},{
    "id": 2,
    'title': 'Example of title',
    'text': 'Description of title'
}]

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')

    return render_template('login.html')
