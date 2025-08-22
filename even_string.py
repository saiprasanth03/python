#Even strings
a=input("Enter a sentence ")
c=a.split()
print(c)
for i in c:
	if len(i)%2==0: 
		print(i)
