#swap first and last element
l=[]
b=int(input("Enter size: "))
for i in range(b):
	a=int(input())
	l.append(a)
print("List is ", l)
temp=l[0]
l[0]=l[b-1]
l[b-1]=temp
print("After swaping: ")
print(l)
