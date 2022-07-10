'''
Write a program to get a string S, Type of conversion (1 - Convert to Lowercase, 2 - Convert to Uppercase) T, and integer P . Convert the case of the letters in the positions which are multiples of P.(1 based indexing).

Input Description:
Given a string S, Type of conversion T, and integer P

Output Description:
Convert the case of the letters and print the string

Sample Input :
ProFiLe
1
2
Sample Output :
Profile
'''

S=list(map(str,input()))
T=int(input())
P=int(input())
l=[]
for i in range(1,len(S)+1):
    if i%P==0:
        if T==1:
            l.append(S[i-1].lower())
        elif T==2:
            l.append(S[i-1].upper())
    else:
        l.append(S[i-1])
print("".join(l))
