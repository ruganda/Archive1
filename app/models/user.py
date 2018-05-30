"""This module defines a user class and methods associated to it"""

class User(object):
    """ A class to handle activities related to a user"""
    def __init__(self):
        # A list to hold all user objects
        self.users_list = []
    
    def register(self,name,username, password,):
        """A method to register users with correct and valid details"""

        # empty dict to hold details of the user to be created
        user_details = {}
        # check if a user with that username exists
        for user in self.users_list:
            if username == user['username']:
                return "Username already exists."
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
