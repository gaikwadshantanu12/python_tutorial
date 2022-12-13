# WAP to check if entered string is upper case, lower case, digit or special symbol and also count

ch = input("Enter the string - ")
c_upper , c_lower , c_digit , c_space , c_symbol = 0,0,0,0,0

for char in ch:
    if char.isupper():
        c_upper += 1
    elif char.islower():
        c_lower += 1
    elif char.isdigit():
        c_digit += 1
    elif char.isspace():
        c_space += 1
    else:
        c_symbol += 1

print("Upper Case - ",c_upper,"\nLower Case - ",c_lower,"\nDigit - ",c_digit,"\nWhite space - ",c_space,"\nSpecial Symbol - ",c_symbol)