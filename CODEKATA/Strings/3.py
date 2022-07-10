'''
You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

Input Description:
You are given a long string of digits

Output Description:
Print the desired result print -1 if result length is 0

Sample Input :
1331
Sample Output :
11
'''

ui=[]
for i in input():
    ui.append(i)
try:
    for i in range(len(ui)):
        if ui[i]==ui[i+1]:
            ui.pop(i)
            ui.pop(i)
except IndexError as e:
    pass
finally:
    print(''.join(str(i) for i in ui))
    