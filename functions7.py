#Reversing the list without slicing
a=[1,3,5,2,9]
def reverse(a):
	l=len(a)
	for i in range(l):
		print(a[l-1-i],end=" ")
reverse(a)
