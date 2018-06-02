"""This module defines a user class and methods associated to it"""
import jwt


class User(object):
    """ A class to handle activities related to a user"""

    def __init__(self):
        self.users_list = []

    def generate_token(self, username):
        """Generates the access token to be used as the Authorization header"""

        try:
            payload = {'username': username}
            jwt_string = jwt.encode(
                payload,
                'donttouch',
                algorithm='HS256'
            )
            return jwt_string

        except Exception as e:
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decode the access token from the Authorization header."""
        try:
            payload = jwt.decode(token, 'hard to guess string')
            return payload['username']
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"

    def register(self, name, username, password,):
        """A method to register users with correct and valid details"""

        user_data = {}
        for user in self.users_list:
            if username == user['username']:
                return "Username already exists."
            if username != user["username"]:
                return "user does not exist"
        else:
            if len(password) < 6:
                return "Password too short"
            else:
                user_data["name"] = name
                user_data['username'] = username
                user_data['password'] = password
                self.users_list.append(user_data)
                return "Registration successfull"
        return "user does not exist"

    def login(self, username, password):
        """A method to register a user given valid user details"""
        for user in self.users_list:
            if username == user["username"] and password == user["password"]:
                return 'Login successful'
            return "invalid username or password"
        return "user does not exist"
