# WAP to find all the values in a list that are greater than a specified number

a = eval(input("Enter list of numbers [] - "))
num = int(input("Enter any number to compare - "))

b = [x for x in a if x>num]
print(b)