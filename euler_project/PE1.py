import sys
import unittest
def sumOfnumberMultiplyOfThreeOrFive(x):
    x -= 1
    x3 = x // 3
    x5 = x // 5
    x15 =x // 15

    sum3 = 3 * x3 *(x3 + 1) / 2
    sum5 = 5 * x5 *(x5 + 1) / 2
    sum15 = 15 * x15 *(x15 + 1)  / 2

    return sum3 + sum5 - sum15




