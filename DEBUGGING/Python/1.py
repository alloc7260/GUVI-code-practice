"""
Given the values of a,b and x in the equation ax + b = y. Find the value of y.

Input Description:-
A single line contains 3 space separated integers.

Output Description:-
Print the value y.

Sample Input :
3 5 2
Sample Output :
11
"""

a,b,x=map(int,input().split())
y=(a*x)+b
print(y)
