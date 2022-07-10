'''
Joyal was given a sentence. His task is to delete the two words that comes together and print the sentence so that the words in the output sentence have distinct words compared to their adjacent words. If no words are present in the output sentence print -1

Input Description:
You are given input string 'S'

Output Description:
Print the all the words that are left in the string 's' so that the words in the output sentence have distinct words compared to their adjacent words. Print -1 if no words are left

Sample Input :
I am john cena cena john
Sample Output :
I am
'''

def fuc(uil):
	try:
		for i in range(len(uil)-1):
		        if uil[i]==uil[i+1]:
		            ui.pop(i)
		            ui.pop(i)
	except IndexError as e:
		pass
	finally:
		return uil

ui = input().split()
for j in range(len(ui)):
    ui=fuc(ui)
print(*ui)
