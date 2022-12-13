# WAP to create set from A to Z

a = set()
for x in range(65,91):          # for x in range(ord('A'), ord('Z')+1):
    a.add(chr(x))

print(a)


"""
a = {chr(x) for x in range(ord('A'), ord('Z')+1)}
"""