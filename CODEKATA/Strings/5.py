'''
You are given a string.Your task is to print only the consonants present in the string without affecting the sentence spacings if present. If no consonants are present print -1

Input Description:
You are given a string ‘s’.

Output Description:
Print only consonants.

Sample Input :
I am shrey 
Sample Output :
 m shry
'''

str=input()
l=[]
for i in range(len(str)):
    if str[i] == 'a' or str[i] == 'A' or str[i] == 'e' or str[i] == 'E' or str[i] == 'i'or str[i] == 'I' or str[i] == 'o' or str[i] == 'O' or str[i] == 'u' or str[i] == 'U':
        continue
    else:
        l.append(str[i])
print("".join(l))
