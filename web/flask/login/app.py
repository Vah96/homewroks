from flask import Flask, redirect, url_for, render_template, request, session
import users
import hashlib

app = Flask(__name__)
app.secret_key = b'secret_key_string'

# @app.context_processor
# def context_processor():
#     return dict(format_price={"a": "aaaa", "b": "bbbb"})


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/sign-up', methods=['GET', 'POST'])
def register():
    register_errors = {}
    register_data = {}
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        register_data['username'] = username
        if not username:
            register_errors['username'] = 'Username is required'
        elif users.check_is_valid_username(username) is False:
            register_errors['username'] = 'Username already exists'
        if not password:
            register_errors['password'] = 'Password is required'
        elif len(password) < 6:
            register_errors['password'] = 'Weak password'

        if password and password != confirm_password:
            register_errors['confirm_password'] = 'Confirm password is not match with password'

        if not register_errors:
            users.register_user(username, password)
            return redirect(url_for('login'))

    return render_template('register.html', errors=register_errors, register_data=register_data)


@app.route('/sign-in', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('profile'))
    login_errors = {}
    login_data = {}
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username:
            login_errors['username'] = 'Username is required'
        if not password:
            login_errors['password'] = 'Password is required'

        if not login_errors:
            auth_user = users.login_user(username, password)
            if auth_user:
                session['user'] = {'id': auth_user['id'], 'username': auth_user['username']}
                return redirect(url_for('profile'))
            else:
                login_errors['form_Error'] = 'Invalid credentials'

    return render_template('login.html', errors=login_errors, login_data=login_data)


@app.route('/profile')
def profile():
    current_user = session.get('user')
    if not current_user:
        return redirect(url_for('login'))
    return render_template('profile.html', current_user=current_user)


@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
    return redirect(url_for('login'))

