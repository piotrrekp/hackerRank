def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

def sumOfEvenFibNumberUnder(n):
    sum = 0
    for i in [x for x in range(n) if x % 3 == 0]:
        x = fib(i)
        if  x < n : sum += x
        else: break
    return sum


calculatedEvenFibNumber = {}


def betterAlgorithm(n):
    i = 0
    sum = 0
    fibNum = evenFibNumber(0)
    while fibNum < n:
        sum += fibNum
        i += 1
        fibNum = evenFibNumber(i)
        calculatedEvenFibNumber[i] = fibNum
    return sum


def evenFibNumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    else:
        if (n - 1) not in calculatedEvenFibNumber:
            a = evenFibNumber(n - 1)
            calculatedEvenFibNumber[n - 1] = a
        else:
            a = calculatedEvenFibNumber[n - 1]
        if (n - 2) not in calculatedEvenFibNumber:
            b = evenFibNumber(n - 2)
            calculatedEvenFibNumber[n - 2] = b
        else:
            b = calculatedEvenFibNumber[n - 2]
        return 4 * a + b