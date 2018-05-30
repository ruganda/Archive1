""" This module contains all the view functions for the auth blue print"""

from flask import jsonify, request, session, make_response
from . import auth
from ..import user_instance
@auth.route('/register/', methods=['POST'])
def register():
    """A route to handle user"""
    if request.method == 'POST':
        data = request.get_json()
        name = data["name"]
        username = data['username']
        password = data['password']
        # pass the details to the register method
        try:
            result = user_instance.register(name,
            username, password)
            if result == "Registration successfull":
                return jsonify(response=result), 201
            else:
                return jsonify(response=result), 409
        except Exception as e:
            response = {
                'message': str(e)
            }
            return jsonify(response), 500
@auth.route("/login/", methods =["POST"])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username =data["username"]
        password = data["password"]
        result = user_instance.login(username,password)
        if result =='Login successful':
            # create a  token
            token = user_instance.generate_token(username)
            return jsonify({"token":str(token)})
        return jsonify({"response": result })

