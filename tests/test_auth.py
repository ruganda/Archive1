
# import unittest
# import json
# from app.auth import views as users
# from app import create_app


# class AuthTestCase(unittest.TestCase):
#     """Test case for the authentication"""

#     def setUp(self):
#         # create app using the flask import and choosing the testing environment from the config
#         self.app = create_app('testing')

#         self.mock_user = {
#             "name": "Muba Ruganda",
#             'username': 'ruganda',
#             'password': 'password'
#         }
#         # bind the app context
#         with self.app.app_context():
#             self.client = self.app.test_client

#         # register user
#         self.register = self.client().post('api/v1/auth/register/',
#                                            content_type='application/json',
#                                            data=json.dumps(self.mock_user))

#         self.login = self.client().post('api/v1/auth/login/',
#                                         content_type='application/json',
#                                         data=json.dumps({'username': 'ruganda',
#                                                          'password': 'password'}))

#     # def test_register_user_successfully(self):
#     #     """Test that a new user can register successfully"""
#     #     self.assertIn(u'Registration successful', str(self.register.data))
#     #     self.assertEqual(self.register.status_code, 201)

#     def test_login_with_credentials(self):
#         """test that a user can sign in with correct credentials"""

#         self.assertIn(u"token", str(self.login.data))
#         self.assertEqual(self.login.status_code, 200)

#     def test_login_no_duplicate_uses(self):
#         """tests that a unique user is added"""

#         response = self.client().post('api/v1/auth/login/',
#                                       content_type='application/json',
#                                       data=json.dumps({'username': 'ruganda',
#                                                        'password': 'password'}))
#         self.assertIn("token", str(response.data))
#         self.assertEqual(response.status_code, 200)
