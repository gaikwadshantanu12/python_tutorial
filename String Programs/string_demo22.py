# WAP to remove duplicate characters from string

s = input("Enter string - ")
res = ""

for i in s:
    if i not in res:
        res = res + i

print(res)