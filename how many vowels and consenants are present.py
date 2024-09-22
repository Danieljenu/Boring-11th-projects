#WAP to read a word from the user and display how many vowels and consenants are present ?
print("This program displays how many vowels and consenants are present in the word " )
v=0
c=0
x=input("Enter your word")
for i in(x):
	if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U" :
		v=v+1
	else:
		c=c+1
print(x,"contains",v,"no of vowels and",c,"no of consenants")