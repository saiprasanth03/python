n=int(input("Enter a number : "))
rev=0
m=n
while(n!=0):
	rem=n%10
	rev=rev*10+rem
	n=n//10
if(m==rev):
	print("Palindrome")
else:
	print("Not a Palindrome")
	
