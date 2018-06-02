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

    # def tearDown(self):
    #     self.app_context.pop()

    def test_request_creation(self):
        """Test API can create a request (POST request)"""
        response = self.client().post('api/v1/Request/',
                                      content_type='application/json',
                                      data=json.dumps(mock_data))

        self.assertEqual(response.status_code, 201)
        self.assertIn('created', str(response.data))

    def test_api_can_fetch_all_requests(self):
        """Test API can fetch all (GET request)."""

        response = self.client().post('api/v1/Request/',
                                      content_type='application/json',
                                      data=json.dumps(mock_data1))

        self.assertEqual(response.status_code, 201)
        response = self.client().get('api/v1/Request/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', str(response.data))

    def test_api_can_get_request_by_id(self):
        """Test API can fetch a single request by using it's id."""
        # post data
        response = self.client().post('api/v1/Request/',
                                      content_type='application/json',
                                      data=json.dumps(mock_data2))
        self.assertEqual(response.status_code, 201)
        # get all
        response = self.client().get('api/v1/Request/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', str(response.data))

        results = json.loads(response.data.decode())

        for request in results:
            result = self.client().get(
                'api/v1/Request/{}'.format(request['request_id']))
            self.assertEqual(result.status_code, 200)
            self.assertIn(request['request_id'], str(result.data))

    def test_request_can_be_modified(self):
        """Test API can modify an existing request. (PUT request)"""
        response = self.client().post('api/v1/Request/',
                                      content_type='application/json',
                                      data=json.dumps(mock_data3))
        self.assertEqual(response.status_code, 201)
        # get all
        response = self.client().get('api/v1/Request/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', str(response.data))

        results = json.loads(response.data.decode())
        for request in results:
            rv = self.client().put(
                'api/v1/Request/{}'.format(request['request_id']),
                content_type='application/json',
                data=json.dumps(mock_edit))
            self.assertIn('request modifyied', str(rv.data))
