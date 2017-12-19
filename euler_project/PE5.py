import math
def isPrime1(n):
    for i in xrange(2,int(math.sqrt(n))+1,1):
        if n % i == 0:
            return False
    else:
        return True
def getAlldividiable(n):
    div = []
    while n != 1:
        for i in range(2,n+1):
            if isPrime1(i) and n% i == 0:
                div.append(i)
                n = n/i
                break
    return div
def primesPower(ll):
    uniq = set(ll)
    ans = []
    for item in uniq:
        number = item **ll.count(item)
        if number not in ans: ans.append(number)
    return  ans

def primesAndPowers(n):
    ans = {}
    i = 2
    while n != 1:
        if n % i == 0:
            if i in ans:
                ans[i] = ans[i] + 1
            else:
                ans[i] = 1
            n /= i
            i = 1
        i += 1
    return ans

def findSmallestDividableNumber(n):
    primes = {}
    for i in range(2,n+1):
        primesFori = primesAndPowers(i)
        for j in primesFori:
            if j not in primes:
                primes[j] = primesFori[j]
            else:
                primes[j] = max(primes[j],primesFori[j])
    multi = 1
    for i in primes:
        multi *= i**primes[i]
    return multi