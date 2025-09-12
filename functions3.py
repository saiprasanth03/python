#Find GCD using function
def find_gcd(a,b):
	gcd=1
	minimum=min(a,b)
	for i in range(1,minimum+1):
		if a%i==0 and b%i==0:
			gcd=i
	return gcd	
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
print("GCD of ",num1 ,"and",num2,"is",find_gcd(num1,num2))
