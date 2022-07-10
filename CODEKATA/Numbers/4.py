'''
You are given a very long integer.Your task is to determine the smallest possible number such that sum of factorial of digits results back in ‘n’. Print -1 if no number is possible

Input Description:
You are given a number ‘n’

Output Description:
Print the smallest number

Sample Input :
145
Sample Output :
145
'''

import math
ui = int(input())
s=[]
for i in range(ui+1):
    l=[]
    for j in str(i):
        l.append(math.factorial(int(j)))
    sum=0
    for k in l:
        sum+=k
    if sum == ui:
        s.append(i)

print(s[0])
