#Even or Odd by using lambda 
n=int(input("Enter a number"))
b=lambda n: "Even" if n%2==0 else "Odd"
print(n," is ",b(n)," number")
