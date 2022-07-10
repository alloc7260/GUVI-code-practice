'''
Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
Sample Testcase :
INPUT
3
2 6
OUTPUT
yes
'''

userInput1 = int(input())
s,e = map(int,input().split(" "))
if userInput1 in range(s,e) :
    print("yes")
else :
    print("no")
