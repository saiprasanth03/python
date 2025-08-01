#reverese
l=[]
b=int(input("Enter size: "))
for i in range(b):
	a=int(input())
	l.append(a)
print("List is ", l)
print("Reverse list is :")
l.reverse()
print(l)
