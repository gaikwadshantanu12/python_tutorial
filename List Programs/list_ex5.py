# WAP to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings

l = eval(input("Enter list elements in [] - "))
count = 0
for x in l:
    if len(x) >= 2 and x[0] == x[-1]:
        count = count + 1

print(count)