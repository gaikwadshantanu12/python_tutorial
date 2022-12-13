# WAP to read 2 strings from user and check if s1 is in s2 or not

s1 = input("Enter 1st string - ")
s2 = input("Enter 2nd string - ")

if s1 in s2:
    print(s1+" is present in "+s2)
else:
    print(s1+" isn\'t present in "+s2)