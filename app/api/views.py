from flask import jsonify, request, session, make_response
from . import api
from ..import request_instance
import uuid


@api.route('/Request/', methods=['POST', "GET"])
def create_request():
    """A route to handle Requests"""
    if request.method == 'POST':
        request_data = request.get_json()
        request_type = request_data['request_type']
        item = request_data["item"]
        description = request_data['description']

        try:
            result = request_instance.create_request(item, request_type, description)
            if result == "Request created":
                return jsonify(response=result), 201
            else:
                return jsonify(response=result), 409
        except Exception as e:
            response = {
                'message': str(e)
            }
            return jsonify(response), 500
    return jsonify(request_instance.fetch_all_requests()),200


@api.route('/Request/<request_id>', methods=['GET'])
def fetch_one_request(request_id):
    """A route to handle request updates"""
    request_id = uuid.UUID(request_id)
    request_object = request_instance.fetch_request_by_id(request_id)
    return jsonify(request_object), 200


@api.route('/Request/<request_id>', methods=['PUT'])
def modify_request(request_id):
    """A route to handle requests modification"""
    request_id = uuid.UUID(request_id)
    request_data = request.get_json()
    item = request_data['item']
    description = request_data['description']
    request_type = request_data['request_type']
    status = request_data['status']
    result = request_instance.modify_request(request_id, item, request_type, description, status)
    if result == "update success":
        return jsonify(response=result), 200
    elif result == "no request with given id":
        return jsonify(response=result), 404
    else:
        return jsonify(response=result), 409
