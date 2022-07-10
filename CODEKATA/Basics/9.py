'''
Find the minimum among 10 numbers.
Sample Testcase :
INPUT
5 4 3 2 1 7 6 10 8 9
OUTPUT
1
'''

import math
list=[]
for i in input().split(" "):
    list.append(int(i))
print(min(list))
