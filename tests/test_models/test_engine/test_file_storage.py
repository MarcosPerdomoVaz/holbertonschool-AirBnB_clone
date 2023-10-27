#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""
    fs = FileStorage()
    def testFilePath(self):
        self.assertIsNotNone(self.fs._FileStorage__file_path)
    def testObjects(self):
        self.assertIsNotNone(self.fs._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
