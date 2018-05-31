import uuid
class Request(object):
    """ A class to handle actions related to requests"""
    
    
    def __init__(self):
        self.requests_list =[]
    
    def create_event(self, id, item, type, category, description):
        """A method to create a new event """

        data = {}
        for request_object in self.requests_list :
            if  id == request_object["id"]:
                return "Request already exists"
            if id !=request_object["id"]:
                return "request not found"
        else:
            data["id"] = id
            data['item'] = item
            data['category'] = category
            data['type'] = type
            data['description'] = description
            self.requests_list .append(data)
            return "Request created"
        return "Request does not exist"
           