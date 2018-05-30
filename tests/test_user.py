"""This module defines tests for the user class and its methods"""
import unittest
from app.models.user import User


class UserTests(unittest.TestCase):
    """Define and setup testing class"""

    def setUp(self):
            """ Set up user object before each test"""
            self.user = User()
    
    def test_isuccessful_registration(self):
        """Test is a user with correct credentials can register sucessfully"""
        res = self.user.register("Mubarak ruganda", "ruganda", "password",)
        self.assertEqual(res, "Registration successfull")


    