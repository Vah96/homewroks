import base64
last_user_id = 2

users = [
    {
        "id": 1,
        "username": "one",
        "password": base64.b64encode("onepass".encode("ascii"))
    },
    {
        "id": 2,
        "username": "two",
        "password": base64.b64encode("twopass".encode("ascii"))
    }
]


def check_is_valid_username(username):
    for user in users:
        if user['username'] == username.lower():
            return False


def register_user(username, password):
    global last_user_id
    last_user_id = last_user_id + 1
    new_user = {
        "id": last_user_id,
        "username": username.lower(),
        "password": base64.b64encode(password.encode("ascii"))
    }
    users.append(new_user)


def login_user(username, password):
    for user in users:
        if user['username'] == username.lower() and user['password'] == base64.b64encode(password.encode("ascii")):
            return {"username": username, "id": user["id"]}
    return False


