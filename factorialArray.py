#!/bin/python

import sys
def firstOperation(A,l,r):
    for i in range(l-1,r):
        A[i] += 1
    return A

def secondOperation(A,l,r):
    sumTot = 0
    for i in range(l-1,r):
        sumTot += silnia(A[i])
    print sumTot % (10**9)
    return sumTot % (10**9)

def thirdOperation(A,i,v):
    A[i-1] = v
    return A

def silnia(n):
    if n>1:
        return n*silnia(n-1)
    elif n in (0,1):
        return 1

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = map(int, raw_input().strip().split(' '))
    for a0 in xrange(m):
       a,b,c =  map(int, raw_input().strip().split(' '))
       if a == 1:
           firstOperation(A,b,c)
       elif a == 2:
           secondOperation(A,b,c)
       elif a == 3:
           thirdOperation(A,b,c)
