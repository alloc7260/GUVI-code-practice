'''
You are given a large number made of only 0’s and 1’s.Your task is to find the max no of consecutive 1’s. If there are no 1’s print -1

Input Description:
A large number ‘n’

Output Description:
Print the max no of consecutive 1 in the number

Sample Input :
101011111
Sample Output :
5
'''

ui = input()
ui= ui.split("0")
ui=list(filter(("").__ne__, ui))
ui.sort()
if ui == []:
    print(-1)
else:
    ui.sort()
    print(len(ui[-1]))
    