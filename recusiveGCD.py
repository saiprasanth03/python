#GCD
gcd=1;
def find_gcd(a,b):
	if b==0:
		return a
	else:
		return find_gcd(b,a%b)
a=int(input("Enter first value"))
b=int(input("Enter second value"))
print("GCD of ",a," ",b," is ",find_gcd(a,b))
