"""This module defines tests for the user class and its methods"""
import unittest
from app.models.user import User


class UserTests(unittest.TestCase):
    """Define and setup testing class"""

    def setUp(self):
            """ Set up user object before each test"""
            self.user = User()

