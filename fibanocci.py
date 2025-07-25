n=int(input("Enter a number(>2) : "))
i=3
print("0")
print("1")
a=0
b=1
while(i<=n):
	temp=a+b
	print(temp)
	a=b
	b=temp
	i+=1
	
