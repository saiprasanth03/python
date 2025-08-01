#even odd
l=[]
b=int(input("Enter size: "))
for i in range(b):
	a=int(input())
	l.append(a)
print("List is ", l)
e=[]
o=[]
for i in range(b):
	if l[i]%2==0:
		e.append(l[i])
	else:
		o.append(l[i])
		
print("Even list is: ")
print(e)
print("Odd list is : ")
print(o)
