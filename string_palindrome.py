#string palindrome
s="MadaM"
a=""
for i in s:
	a=i+a
if(a==s):
	print(s,"string is a palindrome ")
else:
	print(s,"string is not a palindrome ")
