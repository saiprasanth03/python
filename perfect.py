n=int(input("Enter a number : "))
count=0
for i in range(1,n):
	if(n%i==0):
		count+=i
if(count==n):
	print(n," is a perfect number")
else:
	print(n," is not a perfect number")

