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

    def test_duplicate_user(self):
        """Test with an already existing user, try registering a user twice"""
        self.user.register("ruganda", "ruganda@mail.com", "654123", "654123")
        res = self.user.register("ruganda", "ruganda@mail.com", "654123", "654123")
        self.assertEqual(res, "Username already exists.")
