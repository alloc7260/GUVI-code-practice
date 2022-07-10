'''
Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd
'''

import math
n,m = map(int,input().split(" "))
if (n+m)%2==0 :
    print("even")
else:
    print("odd")
    