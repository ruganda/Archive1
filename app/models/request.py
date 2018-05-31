import uuid
class Request(object):
    """ A class to handle actions related to requests"""
    
    
    def __init__(self):
        self.requests_list =[]
    
    def create_request(self, request_id, item, request_type, category, description):
        """A method to create a new event """

        data = {}
        for request_object in self.requests_list :
            if  request_id == request_object["id"]:
                return "Request already exists"
            if request_id !=request_object["id"]:
                return "request not found"
        else:
            data["request_id"] = request_id
            data['item'] = item
            data['category'] = category
            data['type'] = request_type
            data['description'] = description
            self.requests_list .append(data)
            return "Request created"
        return "Request does not exist"
    
    def modify_test(self):
        pass
           