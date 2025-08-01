#add and avg
l=[]
b=int(input("Enter size: "))
for i in range(b):
	a=int(input())
	l.append(a)
print("List is ", l)
print("Sum is :",sum(l))
avg=sum(l)/b
print("Average is :",avg)
