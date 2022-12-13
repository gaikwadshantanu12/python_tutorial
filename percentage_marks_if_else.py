"""WAP to read percentage marks from user and print appropriate message as follows :

Marks           Message
100 to 80       Distinction
60 to <80       First Class
50 to <60       Second Class
40 to <50       Third Class
<40             Fail : Better luck next time

Without using and
"""

marks = eval(input("Enter marks in percentage - "))
if marks >= 80:
    if marks <= 100:
        print("Distinction")
    else:
        print("Percentage Marks cannot be greater than 100")
elif marks >= 60:
    if marks < 80:
        print("First Class")
    else:
        print("Distinction")
elif marks >= 50:
    if marks < 60:
        print("Second Class")
    else:
        print("First Class")
elif marks >= 40:
    if marks < 50:
        print("Third Class")
    else:
        print("Second Class")
elif marks < 40:
    print("Fail : Better Luck Next Time")
else:
    print("Percentage Marks cannot be greater than 100")