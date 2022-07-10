'''
In a firm there is an intelligent employee. He said that he will not work on all those days which has factors more than 2. You are given with month and year calculate the no of working days of employee.

Input Description:
Month(M) and year(Y)

Output Description:
N denoting no of working days

Sample Input :
May 2016
Sample Output :
11
'''

from calendar import *
userInput = input()
il=userInput.split()
month=il[0]
year=int(il[1])

for i in range(1,13):
    if month == month_name[i]:
        monthint=i

a,days = monthrange(year,monthint)
d=[]
for i in range(days):
    factors=[]
    for j in range(1,i+2):
        if (i+1)%j==0:
            factors.append(i)
    if len(factors)<=2:
         d.append(i+1)
print(len(d)-1)
