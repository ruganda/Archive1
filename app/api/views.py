from flask import jsonify, request, session, make_response
from . import api
from ..import request_instance
import jwt
import uuid
from functools import wraps
from ..import user_instance
from ..models.user import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, 'hard to guess string')
            print(data['username'])
            for user in user_instance.users_list:
                if user.get("username"):
                    current_user = user['username']= data['username']
                    
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@api.route('/Request/', methods=['POST', "GET"])
@token_required
def create_request(current_user):
    """A route to handle Requests"""
   
    if request.method == 'POST':
        request_data = request.get_json()
        request_type = request_data['request_type']
        item = request_data["item"]
        description = request_data['description']

        try:
            result = request_instance.create_request(
                item, request_type, description)
            if result == "Request created":
                return jsonify(response=result), 201
            else:
                return jsonify(response=result), 409
        except Exception as e:
            response = {
                'message': str(e)
            }
            return jsonify(response), 500
    return jsonify(request_instance.fetch_all_requests()), 200


@api.route('/Request/<request_id>', methods=['GET'])
@token_required
def fetch_one_request(current_user, request_id):
    """A route to handle request updates"""
    request_id = uuid.UUID(request_id)
    request_object = request_instance.fetch_request_by_id(request_id)
    return jsonify(request_object), 200


@api.route('/Request/<request_id>', methods=['PUT'])
@token_required
def modify_request(current_user,request_id):
    """A route to handle requests modification"""
    request_id = uuid.UUID(request_id)
    request_data = request.get_json()
    item = request_data['item']
    description = request_data['description']
    request_type = request_data['request_type']
    status = request_data['status']
    result = request_instance.modify_request(
                                    request_id, item, request_type,
                                     description, status)
    if result == "update success":
        return jsonify(response=result), 200
    elif result == "no request with given id":
        return jsonify(response=result), 404
    else:
        return jsonify(response=result), 409
