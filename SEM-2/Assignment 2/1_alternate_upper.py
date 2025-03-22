"""Write a program that asks the user to enter a word and then capitalizes every other letter of that word. 
So, if the user enters rhinoceros, the program should print rHiNoCeRoS."""

str=input("Enter a string : ")
res=""
for i in range(len(str)):
	if i%2==1:
		res+=str[i].upper()
	else:
		res+=str[i]
print("Result =",res)	