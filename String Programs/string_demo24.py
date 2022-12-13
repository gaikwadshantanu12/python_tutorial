# WAP to merge characters of 2 strings into single string by taking characters alternatively

s1 = input("Enter 1st string - ")
s2 = input("Enter 2nd string - ")
i = 0
res = ""

while i < len(s1) or i < len(s2):
    if i < len(s1):
        res = res + s1[i]
    if i < len(s2):
        res = res + s2[i]

    i += 1
print(res)