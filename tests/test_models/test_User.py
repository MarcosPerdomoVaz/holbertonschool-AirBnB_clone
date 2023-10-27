#!/usr/bin/python3
"""
testing class base
"""

import unittest
from models.user import User



class test_class_user(unittest.TestCase):
    """class for testing class base model"""
    my_model = User()
    
    def test_type(self):
        self.assertIsInstance(self.my_model, User)

    def test_email(self):
        """sdsadsd d sds s d s """
        self.assertEqual(self.my_model.email, "")
    def test_password(self):
        """sdsadsd d sds s d s """
        self.assertEqual(self.my_model.password, "")

    def test_first_name(self):
        """sdsadsd d sds s d s """
        self.assertEqual(self.my_model.first_name, "")

    def test_last_name(self):
        """sdsadsd d sds s d s """
        self.assertEqual(self.my_model.last_name, "")


if __name__ == '__main__':
    unittest.main()
