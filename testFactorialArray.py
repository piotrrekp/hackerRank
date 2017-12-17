import unittest
from factorialArray import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def test_firstOperation(self):
        A = [1,1,1,1]
        actual = firstOperation(A,2,3)
        expected = [1,2,2,1]
        self.assertEqual(actual,expected)

    def test_secondOperation(self):
            A = [1, 1, 1, 1]
            actual = secondOperation(A, 2, 3)
            expected = 2
            self.assertEqual(actual, expected)
    def test_thirdOperation(self):
        A = [1, 1, 1, 1]
        actual = thirdOperation(A, 2, 3)
        expected = [1, 3, 1, 1]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
