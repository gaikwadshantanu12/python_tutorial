# WAP to remove duplicate words from string

s = input("Enter string - ")
lst = s.split()
res = ""

for w in lst:
    if w not in res:
        res = res + w + " "

print(res)