import json
import unittest
from app import create_app
from app.auth import views
from mock_data import*


class RequestTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client

    # def register_user(self):
    #     return self.client().post('api/v1/auth/register', content_type='application/json', data=json.dumps(test_user1))

    # def login_user(self):
    #     return self.client().post('api/v1/auth/login',content_type='application/json', data=json.dumps(test_login1))

    def get_token(self):
        self.client().post('api/v1/auth/register/',
                           data=json.dumps({
                               "name": "Paul Messi",
                               'username': 'messi',
                               'password': 'password'
                           }),
                           content_type='application/json')
        response = self.client().post('api/v1/auth/login/',
                                      data=json.dumps({
                                          'username': 'messi',
                                          'password': 'password'
                                      }),
                                      content_type='application/json')
        data = json.loads(response.data.decode())
        print(data)
        print(data['token'])
        return data['token']

    def test_fetching_requests_without_token(self):
        """ Tests accessing the request endpoint without a token """
        response = self.client().get('api/v1/Request/')
        self.assertEqual(response.status_code, 401)

    def test_accessing_request_view_with_invalid_or_expired_token(self):
        """ Tests accessing the bucketlist endpoint with an invalid
        or expired token """
        response = self.client().get('api/v1/Request/',
                                     headers={'x-access-token':
                                              'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 401)

    def test_request_creation(self):
        """Test API can create a request (POST request)"""
    with self.test_client() as c:
        rv = c.post('/api/v1/auth/register', json={'test12'
            'username': 'flask', 'password': 'secret'
        })
        json_data = rv.get_json()
        assert verify_token(email, json_data['token'])
        
        response = self.client().post('api/v1/Request/',
                                      content_type='application/json',
                                      data=json.dumps(mock_data),
                                      headers={'x-access-token':self.get_token})

        self.assertEqual(response.status_code, 201)
        self.assertIn('created', str(response.data))

    # def test_api_can_fetch_all_requests(self):
    #     """Test API can fetch all (GET request)."""

    #     response = self.client().post('api/v1/Request/',
    #                                   content_type='application/json',
    #                                   data=json.dumps(mock_data1))

    #     self.assertEqual(response.status_code, 201)
    #     response = self.client().get('api/v1/Request/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('status', str(response.data))

    # def test_api_can_get_request_by_id(self):
    #     """Test API can fetch a single request by using it's id."""
    #     # post data
    #     response = self.client().post('api/v1/Request/',
    #                                   content_type='application/json',
    #                                   data=json.dumps(mock_data2))
    #     self.assertEqual(response.status_code, 201)
    #     # get all
    #     response = self.client().get('api/v1/Request/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('status', str(response.data))

    #     results = json.loads(response.data.decode())

    #     for request in results:
    #         result = self.client().get(
    #             'api/v1/Request/{}'.format(request['request_id']))
    #         self.assertEqual(result.status_code, 200)
    #         self.assertIn(request['request_id'], str(result.data))

    # def test_request_can_be_modified(self):
    #     """Test API can modify an existing request. (PUT request)"""
    #     response = self.client().post('api/v1/Request/',
    #                                   content_type='application/json',
    #                                   data=json.dumps(mock_data3))
    #     self.assertEqual(response.status_code, 201)
    #     # get all
    #     response = self.client().get('api/v1/Request/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('status', str(response.data))

    #     results = json.loads(response.data.decode())
    #     for request in results:
    #         rv = self.client().put(
    #             'api/v1/Request/{}'.format(request['request_id']),
    #             content_type='application/json',
    #             data=json.dumps(mock_edit))
    #         self.assertIn('request modifyied', str(rv.data))
