import unittest
from app import add, minus


class TestApp(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(2, 3), 5)

    def testMinus(self):
        self.assertEqual(minus(2, 3), -1)


if __name__ == "__main__":
    unittest.main()
