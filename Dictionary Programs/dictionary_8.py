# WAP to remove a key from dictionary

d = eval(input("Enter dictionary in 'key:value' pair - \n"))
print(d)
search = eval(input("Enter key to remove - "))
if search in d:
    d.pop(search)
    print("New Dictionary - \n",d)
else:
    print("Key Not Found")