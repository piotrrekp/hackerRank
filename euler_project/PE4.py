import math
def isPalindrome(n):
    a = str(n)
    for i in range(len(str(n))-1):
        if str(a)[i] != str(a)[-i-1]:
            return False
    else:
        return True

def largestPalindromeUnder(n):
    while True:
        n -= 1
        if isPalindrome(n):
            for i in range(100, int(math.sqrt(n))+1):
                # print i
                if n % i == 0 and n/i < 1000:
                    print n, "=", i, "*", n//i
                    return n
