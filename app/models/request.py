import uuid
class Request(object):
    """ A class to handle actions related to requests"""
    
    request_list =[]
    def __init__(self,item =None,category=None, type=None,description =None):
        self.item = item
        self.type =type
        self.description = description