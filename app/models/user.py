"""This module defines a user class and methods associated to it"""
import jwt
class User(object):
    """ A class to handle activities related to a user"""
    def __init__(self):
        # A list to hold all user objects
        self.users_list = []
    
    def generate_token(self, username):
        """Generates the access token to be used as the Authorization header"""

        try:
            # set up a payload with an expiration time
            payload = { 'usernam': username}
            # create the  string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                'donttouch',
                algorithm='HS256'
            )
            return jwt_string

        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decode the access token from the Authorization header."""
        try:
            payload = jwt.decode(token, 'hard to guess string')
            return payload['username']
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"


    def register(self,name,username, password,):
        """A method to register users with correct and valid details"""

        # empty dict to hold details of the user to be created
        user_details = {}
        # check if a user with that username exists
        for user in self.users_list:
            if username == user['username']:
                return "Username already exists."
            if username !=user["username"]:
                return "user does not exist"
        else:
            
            # check for validate password length
            if len(password) < 6:
                return "Password too short"     
            else:
                #register user if all the details are valid
                user_details["name"] = name
                user_details['username'] = username
                user_details['password'] = password
                self.users_list.append(user_details)
                return "Registration successfull"
    
    
        return "user does not exist"
    def login(self, username, password):
        """A method to register a user given valid user details"""
        for user in self.users_list :    
            if username == user["username"] and password == user["password"]:
                return 'Login successful'
            return "invalid username or password"
        return "user does not exist"
