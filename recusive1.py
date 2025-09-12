#factorial of a number
def fact(n):
	if(n==0):
		return 1
	else:
		return n*fact(n-1)
n=int(input("Enter a number: "))
if(n<0):
	print("Factorial does not exist")
else:
	print("Factorial of ",n," is ",fact(n))
