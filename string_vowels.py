#count vowels
v=['a','e','i','o','u','A','E','I','O','U']
vowels=0
consonents=0
a=input("Enter a string ")
for i in a:
	if(i in v):
		vowels += 1
	else:
	 	consonents +=1
print(vowels," vowels in string")
print(consonents," consonents in string")
