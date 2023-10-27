#!/usr/bin/python3
"""
testing class base
"""

import unittest
from models.state import State



class test_class_state(unittest.TestCase):
    """class for testing class base model"""
    my_model = State()

    def testName(self):
        self.assertEqual(self.my_model.name, "")

    def testStateId(self):
        self.assertEqual(self.my_model.state_id, "")
