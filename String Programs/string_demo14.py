# WAP to check if entered character is upper case, lower case, digit or special symbol

ch = input("Enter the character - ")
if len(ch) > 1:
    print("Invalid Entry...\nPlease enter only one character")
else:
    if ch.isupper():
        print("Entered character is in upper case")
    elif ch.islower():
        print("Entered character is in lower case")
    elif ch.isdigit():
        print("Entered character is digit")
    elif ch.isspace():
        print("Entered character is whitespace")
    else:
        print("Entered character is special symbol")