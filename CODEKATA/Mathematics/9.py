'''
boy rolls an unbiased die until he gets ‘1’. You are given a number n find the total sum of probability that he will get ‘1’ on or before nth trial.(Probability of getting 1 at 1 time + probability of getting 1 at 2 trial….+probability of getting 1 at nth trial)

 

Constraints

1<=n<=1000

Input Description:
You are given a number ‘n’.

Output Description:
Print two numbers denoting numerator and denominator

Sample Input :
1
Sample Output :
1 6
'''

ui = int(input())
nu=6**ui - 5**ui
de=6**ui
print("{} {}".format(nu,de))
