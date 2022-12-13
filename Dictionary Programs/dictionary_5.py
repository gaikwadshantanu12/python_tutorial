# WAP to read a value and print all keys for which given value matches

d = eval(input("Enter dictionary in 'key:value' pair - \n"))
search = eval(input("Enter value to search - "))

for key,value in d.items():
    if value == search:
        print(key,end=" ")

