import unittest
from PE1 import *
from PE2 import *
from PE3 import *
from PE4 import *
from PE5 import *
from PE7 import *
class MyTestPE1(unittest.TestCase):
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

class MyTestPE2(unittest.TestCase):
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
class MyTestPE3(unittest.TestCase):
    def test_PE3_1(self):
        actual = largestPrimeFactor(17)
        expected = 17
        self.assertEqual(actual, expected)

    def test_PE3_2(self):
        actual = largestPrimeFactor(10)
        expected = 5
        self.assertEqual(actual, expected)

    def test_PE3_3(self):
        actual = largestPrimeFactor(16)
        expected = 2
        self.assertEqual(actual, expected)

    def test_PE3_4(self):
        actual = isPrime(2)
        expected = True
        self.assertEqual(actual, expected)

    def test_PE3_5(self):
        actual = largestPrimeFactor(179426549*2)
        expected = 179426549
        self.assertEqual(actual, expected)

class MyTestPE4(unittest.TestCase):
    def test_PE4_1(self):
        actual = isPalindrome(100001)
        expected = True
        self.assertEqual(actual, expected)

    def test_PE4_2(self):
        actual = isPalindrome(1)
        expected = True
        self.assertEqual(actual, expected)

    def test_PE4_3(self):
        actual = isPalindrome(10101)
        expected = True
        self.assertEqual(actual, expected)

    def test_PE4_4(self):
        actual = largestPalindromeUnder(101110)
        expected = 101101
        self.assertEqual(actual, expected)

    def test_PE4_5(self):
        actual = largestPalindromeUnder(800000)
        expected = 793397
        self.assertEqual(actual, expected)

class MyTestPE5(unittest.TestCase):
    def test_1(self):
        actual = findSmallestDividableNumber(3)
        expected = 6
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = getAlldividiable(10)
        expected = [2, 5]
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = getAlldividiable(140)
        expected = [2,2,5, 7]
        self.assertEqual(actual, expected)

    def test_4(self):
        actual = primesPower(getAlldividiable(24))
        expected = [3,8]
        self.assertEqual(actual.sort(), expected.sort())

    def test_5(self):
        actual = findSmallestDividableNumber(10)
        expected = 2520
        self.assertEqual(actual, expected)

    def test_6(self):
        actual = findSmallestDividableNumber(3)
        expected = 6
        self.assertEqual(actual, expected)

    def test_7(self):
        actual = findSmallestDividableNumber(5)
        expected = 60
        self.assertEqual(actual, expected)
        actual = findSmallestDividableNumber(6)
        self.assertEqual(actual, expected)
    def test_10(self):
        actual = findSmallestDividableNumber(7)
        expected = 420
        self.assertEqual(actual, expected)

    def test_12(self):
        actual = findSmallestDividableNumber(8)
        expected = 840
        self.assertEqual(actual, expected)

    def test_11(self):
        actual = findSmallestDividableNumber(10)
        expected = 2520
        self.assertEqual(actual, expected)
        actual = findSmallestDividableNumber(9)
        self.assertEqual(actual, expected)

    def test_8(self):
        actual = findSmallestDividableNumber(20)
        expected = 232792560
        self.assertEqual(actual, expected)
    def test_13(self):
        actual = findSmallestDividableNumber(1)
        expected  = 1
        self.assertEqual(actual, expected)
    def testglupoty(self):
        self.assertEqual(True, isPrime1(37))
    def test_9(self):
        actual = primesPower(getAlldividiable(39))
        expected  = [3,13]
        self.assertEqual(actual, expected)
    def testPrimesAndPower(self):
        actual = primesAndPowers(4)
        expected = {2: 2}
        self.assertEqual(actual, expected)

        actual = primesAndPowers(40)
        expected = {2: 3,5:1}
        self.assertEqual(actual, expected)

class MyTestPE7(unittest.TestCase):
    def test_0(self):
        actual = isPrime1()
    def test_1(self):
        actual = getNthPrimeNumber(1)
        expected = 2
        self.assertEqual(actual, expected)
        actual = getNthPrimeNumber(3)
        expected = 5
        self.assertEqual(actual, expected)
        actual = getNthPrimeNumber(6)
        expected = 13
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
