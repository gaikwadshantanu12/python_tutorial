# WAP to insert a given string at the beginning of all items

a = eval(input("Enter list of numbers [] - "))
s = input("Enter string to append - ")
b=[]

for i in a:
    b.append(s+str(i))

print(b)