import unittest
from PE1 import *
from PE2 import *

class MyTestCase(unittest.TestCase):
    def test_PE1_1(self):
        actual = sumOfnumberMultiplyOfThreeOrFive(10)
        expected = 23
        self.assertEqual(expected,actual)
    def test_PE1_2(self):
        actual = sumOfnumberMultiplyOfThreeOrFive(0)
        expected = 0
        self.assertEqual(expected,actual)
    def test_PE1_3(self):
        actual = sumOfnumberMultiplyOfThreeOrFive(3)
        expected = 0
        self.assertEqual(expected,actual)
    def test_PE1_4(self):
        actual = sumOfnumberMultiplyOfThreeOrFive(5)
        expected = 3
        self.assertEqual(expected,actual)
    def test_PE2_1(self):
        actual = sumOfEvenFibNumberUnder(10)
        expected = 10
        self.assertEqual(actual,expected)
    def test_PE2_2(self):
        actual = sumOfEvenFibNumberUnder(100)
        expected = 44
        self.assertEqual(actual,expected)
    def test_PE2_3(self):
        actual = betterAlgorithm(10)
        expected = 10
        self.assertEqual(actual, expected)
    def test_PE2_4(self):
        actual = betterAlgorithm(100)
        expected = 44
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
