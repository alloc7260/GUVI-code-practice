'''
You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. Your task is to help the authority in finding the common ids.

Input Description:
First line contains a number ‘n’ representing no of prisoners. Next line contains n space separated numbers.

Output Description:
Print the ids which are not unique. Print -1 if all ids are unique

Sample Input :
7
1 1 11 121 131 141 98
Sample Output :
1
'''

dc = input()
uil=sorted(list(map(int,input().split())))
new = []
for a in uil: 
    n = uil.count(a) 
    if n > 1:        
        if new.count(a) == 0:
            new.append(a)
print(*new)
