"""WAP to check whether two lists are circularly identical or not

Note - Execute Each Step in IDLE

Algorithm -

S1 - Convert Two Lists Into String
S2 - Double First List
S3 - And after duple operation, if List 2 is present in List 1 as a substring at least 1 time,
    then  the are circularly identical
"""

a = eval(input("Enter List No. 1 in [] - "))
b = eval(input("Enter List No. 2 in [] - "))

# Converting 'a' list to string
a = [str(x) for x in a]                 # Here All Elements are converted to string
# Join the list 'a' into string
a = "".join(a)

# Converting 'b' list to string
b = [str(x) for x in b]                 # Here All Elements are converted to string
# Join the list 'b' into string
b = "".join(b)

if b in a*2:
    print("Both Are Circularly Identical...")
else:
    print("Both Are Not Circularly Identical...")