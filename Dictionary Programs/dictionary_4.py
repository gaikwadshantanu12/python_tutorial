# WAP to check whether a given key already exists in a dictionary

d = eval(input("Enter dictionary in 'key:value' pair - \n"))
search = eval(input("Enter key to search - "))
if search in d:
    print("Key Found and Value is",d[search])
else:
    print("Key Not Found")