#remove first duplicate
l=[]
n=int(input("Enter size: "))
for i in range(n):
	a=int(input())
	l.append(a)
print("List is ",l)
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if(l[i]==l[j]):
			l.pop(i)
			break
		else:
			continue
		break
print(l)
