from storage import load_data, save_data

USERS_FILE = "users.json"


class UserSystem:

    def __init__(self):
        self.users = load_data(USERS_FILE, [])

    def save(self):
        save_data(USERS_FILE, self.users)

    def register(self, username, password):
        if len(password) < 6:
            return False, "Password must be at least 6 characters."

        for user in self.users:
            if user["username"] == username:
                return False, "Username already exists."

        self.users.append({
            "username": username,
            "password": password
        })

        self.save()
        return True, "Registration successful."

    def login(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return True
        return False
