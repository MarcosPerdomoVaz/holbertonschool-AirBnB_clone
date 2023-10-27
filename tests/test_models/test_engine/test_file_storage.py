#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""
    def testFilePath(self):
        self.assertIsNotNone(FileStorage.__file_path)
    def testObjects(self):
        self.assertIsNotNone(FileStorage.__objects)
