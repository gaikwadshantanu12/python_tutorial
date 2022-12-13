# WAP to remove words beginning with vowels

name = input("Enter list separated with space - ")
lst = name.split()
res =""
for i in lst:
    if i[0].lower() not in 'aeiou':
        res = res + i + " "

print(res)