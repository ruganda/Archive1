import uuid
class Request(object):
    """ A class to handle actions related to requests"""
    
    
    def __init__(self):
        self.requests_list =[]
    
    def existing_request(self, description, item):
        """A method to check if a user already has the a the same requests in her requests"""
        for request_object in self.requests_list:
            if request_object['description'] == description and request_object['item'] == item:
                    return True
        else:
            return False

    def create_request(self,item, request_type, description):
        """A method to create a new request """
        self.data = {}
        if self.existing_request(description, item):
            return "request already exists"
        else:
            self.data['item'] = item
            self.data['request_id'] = uuid.uuid1()
            self.data['type'] = request_type
            self.data['description'] = description
            self.data["status"] = "new"
            self.requests_list.append(self.data)
            return "Request created"
        return "Request does not exist"
    
    def fetch_all_requests(self):
        "a method to fetch all requests"
        return self.requests_list 

    def fetch_request_by_id(self, request_id):
        """A method to f given an title of a request"""
        for request_object in self.requests_list:
            if request_object['request_id'] == request_id:
                return request_object
        return False
    
    def modify_request(self, request_id, item, request_type, description, status):
        """ Find a request with the given id and modify its details"""
        
        for request_object in self.requests_list:
            if request_object['request_id'] == request_id:
                self.requests_list.remove(request_object)             
                request_object['item'] = item
                request_object['request_type'] = request_type
                request_object['description'] = description
                request_object['status'] = status
                request_object['request_id'] = request_id
                self.requests_list.append(self.data)
                return "request modifyied"
        else:
            return "no request with given id"
    
           