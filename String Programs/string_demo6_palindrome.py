# WAP to check if given string is palindrome or not

s1 = input("Enter String - ")

if s1.lower() == s1[::-1].lower():
    print(s1+" is Palindrome")
else:
    print(s1+" isn\'t Palindrome")