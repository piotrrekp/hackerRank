import unittest

import math

primeList = []

def isPrime1(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in xrange(2,int(math.sqrt(n))+1,1):
        if n % i == 0:
            return False
    else:
        return True


def getNthPrimeNumber(n):
    counter = len(primeList)
    if counter > n:
        return primeList[n-1]
    else:
        if counter != 0:
            i = primeList[-1]
        else:
            i = 1
        while counter != n:
            i += 1
            if isPrime1(i):
                counter += 1
                primeList.append(i)
        return primeList[-1]

class MyTestPE7(unittest.TestCase):

    def test_0(self):
        actual = isPrime1(49)
        expected = False
        self.assertEqual(actual,expected)
    def test_1(self):
        actual = getNthPrimeNumber(1)
        expected = 2
        self.assertEqual(expected,actual)
    def test_2(self):
        actual = getNthPrimeNumber(2)
        expected = 3
        self.assertEqual(actual, expected)
    def test_3(self):
        actual = getNthPrimeNumber(6)
        expected = 13
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
