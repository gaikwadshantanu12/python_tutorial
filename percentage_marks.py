"""WAP to read percentage marks from user and print appropriate message as follows :

Marks           Message
100 to 80       Distinction
60 to <80       First Class
50 to <60       Second Class
40 to <50       Third Class
<40             Fail : Better luck next time

Using and
"""

marks = eval(input("Enter marks in percentage - "))
if marks >= 80 and marks<=100:
    print("Distinction")
elif marks >= 60 and marks<80:
    print("First Class")
elif marks >=50 and marks<60:
    print("Second Class")
elif marks >=40 and marks<50:
    print("Third Class")
elif marks<40:
    print("Fail : Better Luck Next Time")
else:
    print("Please enter marks in range from 0 to 100")