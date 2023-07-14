import json


def check_login(username, password):
    with open("app/data/users.json") as f:
        data = json.load(f)
        users = data["users"]
        for user in users:
            if user["username"] == username and user["password"] == password:
                return True
        return False
