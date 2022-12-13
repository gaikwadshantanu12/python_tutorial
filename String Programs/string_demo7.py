# WAP to read a character and check if it is vowel or not

"""
#Method 1
ch = input("Enter character - ")
if ch == 'a' or ch == 'e' or ch =='i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch =='I' or ch == 'O' or ch == 'U':
    print(ch+" is a vowel")
else:
    print(ch+" isn\'t vowel")

"""

#Method 2
ch = input("Enter character - ")
if ch.lower() in 'aeiou':
    print(ch + " is a vowel")
else:
    print(ch + " isn\'t vowel")
