d = {1:"one",2:"two",3:"three",4:"four"}
print(d)
variable = input("Enter a key")
if(variable in d):
    print("Key exists")
else:
    print("Key does exists")