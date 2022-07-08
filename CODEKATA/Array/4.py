'''
A person saves his monthly saving according to given schema. He saves same amount of money which is equal to the money saved in immediate previous two months. Assume, initially he saved 1000 rupees and in first month he saved another 1000. Your task is to tell how much he had totally saved at the end of ‘n’ months

Input Description:
You will be given a number ‘n’->No. of months

Output Description:
Print the total savings at the end of ‘n’ months

Sample Input :
1
Sample Output :
2000
'''

i_0=0
i0=1000
i1=1000
# fibonacci with threesum
n = int(input())

def fibonacci(n, a, b, c):
    if n == 1:
        return a+b+c
    new = a+b+c
    a=b
    b=c
    c=new
    return(fibonacci(n-1,a,b,c))
    
print(fibonacci(n,i_0,i0,i1))
