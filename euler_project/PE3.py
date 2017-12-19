import math
primeList = {}
def isPrime(n):
    if n in primeList:
        return primeList[n]
    else:
        for i in xrange(2,int(math.sqrt(n))+1,1):
            if n % i == 0:
                primeList[n] = False
                return False
        else:
            primeList[n] = True
            return True

def largestPrimeFactor(n):
    i = 0
    maxPrime = 1
    while n != 1:
        if isPrime(n) == True:
            maxPrime = n
            break
        i += 1
        if n % i == 0:
            n = n / i
            if isPrime(i) == True:
                maxPrime = i
                i = 1
    return maxPrime
