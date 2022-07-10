'''
Rahul is given a task to manipulate a string, He hired you as a developer your task is to delete all the repeating characters and print the result left.

Input Description:
You are given a string ‘s’

Output Description:
Print the remaining string

Sample Input :
mississipie
Sample Output :
mpe
'''

ui=[]
for i in input():
    ui.append(i)
count = {}
for i in ui:
	count[i] = count.get(i, 0) + 1
l=[]
for i in count:
	if count[i]==1:
		l.append(i)
print("".join(l))
