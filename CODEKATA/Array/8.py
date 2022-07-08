'''
Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.

Input Size : N <= 100000

Sample Testcase :
	INPUT
	2143

	OUTPUT
	1 3
'''

ui = list(map(int,input()))
l=[]
for i in ui:
    if not i%2==0:
        l.append(i)
if not l==[]:
    print(*l)
else:
    print(-1)
    