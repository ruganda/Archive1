
import unittest
import json
from app.auth import views 
from app import create_app

class APITestCase(unittest.TestCase):
    """Test case for the authentication"""

    def setUp(self):
        # create app using the flask import and choosing the testing environment from the config
        self.app = create_app('testing')
        
        self.mock_data = {
            "item":"laptop",
            'request_type': 'Maintenance',
            'category': 'electronics',
            'description': 'The machine is to slow ',
            "status": "new"
        }
        # bind the app context
        with self.app.app_context():
            self.client = self.app.test_client

        # create a request
        self.request = self.client().post('api/v1/Request/',
                                      content_type='application/json',
                                      data=json.dumps(self.mock_data))

    
    
    def test_request_can_be_created(self):
        """test that a user can create a request"""
        self.assertEqual(self.request.status_code, 201)

