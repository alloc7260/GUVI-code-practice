'''
You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.

 

Note:Both numbers lie in range 1<=a,b<n

Input Description:
You are given a number ‘n’

Output Description:
Print the number of pairs satisfying above condition

Sample Input :
5
Sample Output :
4

'''

n = int(input())

def getPairsCount(arr, n, sum):
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

r=range(1,n)

print(getPairsCount(r, len(r), n))
