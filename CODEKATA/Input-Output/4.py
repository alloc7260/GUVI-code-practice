'''
Write a code to get the input in the given format and print the output in the given format

Input Description:
First-line indicates two integers separated by space. Second-line indicates two integers separated by space. Third-line indicates two integers separated by space.

Output Description:
Print the input in the same format.

Sample Input :
2 4
2 4
2 4
Sample Output :
2 4
2 4
2 4
'''

for i in range(3):
    i1,i2 = map(int,input().split())
    print(i1,i2)
   