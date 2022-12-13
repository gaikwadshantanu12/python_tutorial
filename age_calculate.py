# WAP to read birthday (day,month,year) and calculate age

from datetime import date
day, month, year = [int(x) for x in input("Enter day,month,year : ").split(",")]
dob = date(year,month,day)
age = int((date.today() - dob).days/365.25)
print(f"Your age is {age}")