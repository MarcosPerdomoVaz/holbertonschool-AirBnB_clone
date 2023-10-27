#!/usr/bin/python3
"""
testing class base
"""

import unittest
from models.review import Review



class test_class_review(unittest.TestCase):
    """class for testing class base model"""
    my_model = Review()

    def testUserId(self):
        self.assertEqual(self.my_model.user_id, "")
    def testPlaceId(self):
        self.assertEqual(self.my_model.place_id, "")
    def testText(self):
        self.assertEqual(self.my_model.text, "")
