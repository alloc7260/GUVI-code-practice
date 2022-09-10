'''
Dityan is alloted with a task. He is provided with some positive numbers. He has to tell the smallest positive natural number(greater than the minimum number present in the list) and in addition to it,the number should not be present in the list and it should not be equal to the sum of any combination of ‘n’ numbers present in the list.You have to develop a suitable program in order to find that number ‘m’.

Input Description:
First line contains a number ‘n’ . next line contains ‘n’ space separated numbers.

Output Description:
print the smallest positive number ‘m’.

Sample Input :
5
1 2 10 12 13
Sample Output :
4
'''

from itertools import combinations
dc = int(input())
il = (input()).split()
l=[]
for i in il:
    l.append(int(i))
mnl=(sorted(l)[0])
comb=[]
sums=set()
for i in range(1,len(l)+1):
	comb.append(combinations(l, i))
for i in list(comb):
    for j in list(i):
    	sums.add(sum(j))
# n>1 and n>mnl
# n not in list
# n not in list(sums)
n=0
while 1:
	if (n>1) and (n>mnl) and (n not in l) and (n not in list(sums)):
		print(n)
		break
	n+=1