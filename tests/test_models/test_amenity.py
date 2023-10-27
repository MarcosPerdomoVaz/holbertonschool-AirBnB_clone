#!/usr/bin/python3
"""
testing class base
"""

import unittest
from models.amenity import Amenity



class test_class_amenity(unittest.TestCase):
    """class for testing class base model"""
    my_model = Amenity()

    def testName(self):
        self.assertEqual(self.my_model.name, "")
