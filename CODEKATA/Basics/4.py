'''
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0
'''

il1 = input().split(" ")
il2 = input().split(" ")
if il1[1] in il2 :
    if il2.count(il1[1]) == 1:
        print(0)
    else :
        print(il2.count(il1[1]))
else :
    print(-1)
