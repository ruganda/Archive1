import unittest
import json
from app import create_app
from app.auth import views


from mock_data import mock_user1, mock_user2, mock2_login


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client

    # def tearDown(self):
    #     self.app_context.pop()

    def test_registration(self):
        """Test user registration works correcty."""
        response = self.client().post('api/v1/auth/register/',
                                      content_type='application/json',
                                      data=json.dumps(mock_user1))

        self.assertEqual(response.status_code, 201)
        self.assertIn('Registration successful', str(response.data))
      
    def test_login_with_credentials(self):
        """test that a user can sign in with correct credentials"""
        self.client().post('api/v1/auth/register/',
                            content_type='application/json',
                            data=json.dumps(mock_user2))
        response = self.client().post('api/v1/auth/login/',
                                      content_type='application/json',
                                      data=json.dumps(mock2_login))
        self.assertIn(u"token", str(response.data))
        self.assertEqual(response.status_code, 200)

    # def test_login_no_duplicate_uses(self):
    #     """tests that a unique user is added"""

    #     response = self.client().post('api/v1/auth/login/',
    #                                   content_type='application/json',
    #                                   data=json.dumps({'username': 'ruganda',
    #                                                    'password': 'password'}))
    #     self.assertIn("token", str(response.data))
    #     self.assertEqual(response.status_code, 200)
     
