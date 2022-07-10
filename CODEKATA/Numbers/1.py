'''
You are given a number ‘n’. You have to tell whether a number is great or not. A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

m+j=n

 

Input Description:
You are given a number n;

Output Description:
Print Great if a number is great else print the no

Sample Input :
59
Sample Output :
Great
'''

ui = int(input())
sum = 0
prod = 1
for digit in str(ui): sum += int(digit)
for digit in str(ui): prod *= int(digit)
if sum+prod==ui: print("Great")
else: print("no")
