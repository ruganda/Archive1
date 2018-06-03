"""This module defines a user class and methods associated to it"""



class User(object):
    """ A class to handle activities related to a user"""

    def __init__(self):
        self.users_list = []
    
    def register(self, name, username, password,):
        """A method to register users with correct and valid details"""

        user_data = {}
        for user in self.users_list:
            if username == user['username']:
                return "User already exists."
            
        else:
            if len(password) < 6:
                return "Password too short"
            else:
                user_data["name"] = name
                user_data['username'] = username
                user_data['password'] = password
                self.users_list.append(user_data)
                return "Registration successfull"


    def login(self, username, password):
        """A method to register a user given valid user details"""
        for user in self.users_list:
            if username == user["username"] and password == user["password"]:
                return 'Login successful'
            return "invalid username or password"
        return "user does not exist"
