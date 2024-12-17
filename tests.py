import unittest
from app import add, minus, multiply


class TestApp(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(2, 3), 5)

    def testMinus(self):
        self.assertEqual(minus(2, 3), -1)

    def testMultiply(self):
        self.assertEqual(multiply(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
