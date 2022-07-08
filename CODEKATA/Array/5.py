'''
You are given an array. Your task is to sort the array in given manner. Print the elements in increasing order of the frequency. If frequency is same print smaller one first.

Input Description:
You are given a number ‘n’. Then in next line n space separated numbers.

Output Description:
Print the array as mentioned

Sample Input :
4
1 1 3 2
Sample Output :
2 3 1
'''

dc=input()
uil=sorted(list(map(int,input().split())))
count = {}
for i in uil:
	count[i] = count.get(i, 0) + 1
ans=sorted(count.items(), key =lambda kv:(kv[1], kv[0]))
l=[]
for i in ans:
	l.append(i[0])
print(*l)
