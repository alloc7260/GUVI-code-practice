'''
A ‘zx’ number is a number which is formed from the sum of 3 numbers ,and the three numbers are such that their hcf equal to 1.

You are given a number.You have to tell whether the number is ‘zx’ or not,if yes then print the three numbers else 0

Input Description:
You are given a number ‘n’

Output Description:
Print the three numbers if n is ‘zx’ number in ascending order else 0

Sample Input :
7
Sample Output :
2 3 2
'''

"""
What does it mean when HCF is 1?
Co-prime numbers or relatively prime numbers are those numbers that have their HCF (Highest Common Factor) as 1. In other words, two numbers are co-prime if they no common factor other than 1.
"""

"""
This question is crazy so i submitted a forum on guvi and leaved it with some code snippets
"""

"""
# ACCEPTING ANSWER ON GUVI
def fuc(ui):
    ll=[]
    for i in range(2,ui):
        for j in range(2,i//2+1):
            if i%j==0:
                break 
        else:
            ll.append(i)

    f=0
    for i in ll:
        for j in ll:
            for k in ll:
                if i+j+k==ui and i==j==k:
                    f=1
                    return [i,j,k]
    if f!=1:
        for i in ll:
            for j in ll:
                for k in ll:
                    if i+j+k==ui and i==k!=j:
                        return [i,j,k]

l=fuc(int(input()))
if l==None:
    print(0)
else :
    print(*l)
"""

"""
# RIGHT ANSWER OF QUESTION (MY)
import math
ui = int(input())
l=[]
for i in range(2,ui):
    for j in range(2,ui):
        for k in range(2,ui):
            if math.gcd(math.gcd(i,j),k)==1 and i+j+k==ui:
                l.append(i)
                l.append(j)
                l.append(k)
                break
        break
    break

if l!=[]:
    print(*sorted(l))
else:
    print(0)
"""

"""
# RIGHT ANSWER OF QUESTION
import math
n=int(input())
s=[]
for i in range(2,n):
    for j in range(2,n):
        for k in range(2,n):
            if math.gcd(math.gcd(i,j),k)==1 and (i+j+k)==n:
                s.append(i)
                break
        s.append(j)
        break
    s.append(k)
    break

if s!=[]:
    print(*sorted(s))
else:
    print(0)
"""

"""
# ALL POSSIBILITIES WITH POSITIVE NUMBERS GREATER THAN 1 (FROM 2 ONWARDS)
import math
ui = int(input())
for i in range(2,ui):
    for j in range(2,ui):
        for k in range(2,ui):
            if math.gcd(math.gcd(i,j),k)==1 and i+j+k==ui:
                print(i,j,k)
"""

"""
# ALL POSSIBILITIES WITH NATURAL NUMBERS (FROM 1 ONWARDS)
import math
ui = int(input())
for i in range(1,ui):
    for j in range(1,ui):
        for k in range(1,ui):
            if math.gcd(math.gcd(i,j),k)==1 and i+j+k==ui:
                print(i,j,k)
"""

"""
# ALL POSSIBILITIES WITH WHOLE NUMBERS (FROM 0 ONWARDS)
import math
ui = int(input())
for i in range(ui):
    for j in range(ui):
        for k in range(ui):
            if math.gcd(math.gcd(i,j),k)==1 and i+j+k==ui:
                print(i,j,k)
"""

"""
