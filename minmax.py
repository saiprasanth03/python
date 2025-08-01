#min max position
l=[]
b=int(input("Enter size: "))
for i in range(b):
	a=int(input())
	l.append(a)
print("List is ", l)
a1=0
a2=0
minimum=min(l)
maximum=max(l)
for i in range(b):
	if(l[i]==minimum):
		a1=i
	if(l[i]==maximum):
		a2=i
print("Minimum index is ",a1,"Value is ",minimum)
print("Maximum index is ",a2,"Value is ",maximum)
