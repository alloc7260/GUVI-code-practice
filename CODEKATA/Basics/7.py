'''
Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes
'''

import math
a,b = map(int,input().split(" "))

def isPerfectSquare(x):
    if(x >= 0):
        sr = math.sqrt(x)
        return ((sr*sr) == float(x))
    return false

if (isPerfectSquare(a*b)):
    print("yes")
else:
    print("no")
    