# WAP that accepts a string and count the number of upper case letters and lower case letters through function

def countAlphabets(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    return lower,upper

lower_case, upper_case = countAlphabets(input("Enter any string : "))
print(f"\n\nUpper case letters are {upper_case}")
print(f"Lower case letters are {lower_case}")
