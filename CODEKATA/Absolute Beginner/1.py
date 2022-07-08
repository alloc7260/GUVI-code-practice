'''
You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.

Input Description:
A number "A" representing some distance in kilometer is provided to you as the input.

Output Description:
Convert and print this value in meters and centimeters.

Sample Input :
2

Sample Output :
2000
200000
'''

userInput = int(input())
#print(f"The Input Provided is {userInput} Kilometers")
print(userInput*1000) #Meters
print(userInput*100000) #Centimeters
