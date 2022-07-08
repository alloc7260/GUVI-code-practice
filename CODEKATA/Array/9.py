'''
You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

Input Description:
First line contains a number ‘n’. Then next line contains n space separated numbers.

Output Description:
Print the difference of indices of largest and smallest array

Sample Input :
5
1 6 4 0 3
Sample Output :
-2
'''

n=int(input())
ui = input()
il=ui.split()
list=[]
for i in il:
    list.append(int(i))
a=list
min=a.index(min(a))
max=a.index(max(a))
print(max-min)
