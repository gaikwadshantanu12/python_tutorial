# WAP to swap first and second half of the string

# if input string - abcd
# output string - cdab

s = input("Enter any string - ")
s1 = s[:len(s)//2]
s2 = s[len(s)//2:]

print(s2+s1)