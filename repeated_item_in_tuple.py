# WAP to find repeated items of tuple

a = eval(input("Enter numeric tuple - "))
b = [x for x in a if a.count(x)>1]
"""
b = []
for x in a:
    if a.count(x)>1:
        b.append(x)
"""
c =[]
for x in b:
    if x not in c:
        c.append(x)

print(f"Repeated Items are {c}")