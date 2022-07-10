'''
You are given a paragraph.Your task is to print the words that come just after articles.

Input Description:
You are given a string ‘s’

Output Description:
print the words that come just after articles and -1 if there are no articles

Sample Input :
The sun rises in the east

Sample Output :
sun east
'''

ui=input().split()
l=[]
for i in range(len(ui)):
    if ui[i-1] in ["a","an","the","A","An","The"]:
        l.append(ui[i])
if l==[]:
    print(-1)
else:
    print(*l)
    