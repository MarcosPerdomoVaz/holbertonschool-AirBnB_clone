import unittest
from models.base_model import BaseModel

class Test(unittest.TestCase):
    def test_base_model(self):
        base = BaseModel()
        self.assertEqual(base.__str__(), f"[{type(base).__name__}] ({base.id}) {base.__dict__}")

if __name__ == '__main__':
    unittest.main()
