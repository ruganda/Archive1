
import unittest
import json
from app.auth import views as users
from app import create_app


class AuthTestCase(unittest.TestCase):
    """Test case for the authentication"""

    def setUp(self):
        # create app using the flask import and choosing the testing environment from the config
        self.app = create_app('testing')
        
        self.user_data = {
            "name":"Muba Ruganda",
            'username': 'ruganda',
            'password': 'password'
        }
        # bind the app context
        with self.app.app_context():
            self.client = self.app.test_client

        # register user
        self.register = self.client().post('/api/v1/auth/register',
                                      content_type='application/json',
                                      data=json.dumps(self.user_data))

        self.login = self.client().post('/api/v1/auth/login',
                                        content_type='application/json',
                                        data=json.dumps({'username': 'ruganda',
                                                             'password': 'password'}))

        self.result = json.loads(self.login.data.decode())

    def test_register_user_successfully(self):
        """Test that a new user can be added"""
        self.assertIn(u'Registration successful', str(self.register.data))
        self.assertEqual(self.register.status_code, 201)