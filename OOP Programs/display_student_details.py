# WAP to define class student.
# Use setDetails method to set information and getDetails method to get information

class student:
    def set_details(self,name,roll_no,gender,seat_no,enroll_no,city):
        # If use multiple input method then we have to convert roll no, seat no & enrollment no to integer : self.roll_no = int(roll_no)
        self.name = name
        self.roll_no = roll_no
        self.gender = gender
        self.seat_no = seat_no
        self.enroll_no = enroll_no
        self.city = city

    def get_details(self):
        print("\n\nName             :",self.name)
        print("Roll No          :", self.roll_no)
        print("Gender           :", self.gender)
        print("Seat No          :", self.seat_no)
        print("Enrollment No    :", self.enroll_no)
        print("City             :", self.city)


# For Single Input
name = input("Enter Name : ")
roll_no = int(input("Enter Roll No : "))
gender = input("Enter Gender : ")
seat_no = int(input("Enter Seat No : "))
enroll_no = int(input("Enter Enrollment No : "))
city = input("Enter City : ")

# For Multiple Input
"""
info = input("Enter Name, Roll No, Gender, Seat No, Enrollment No, City : ").split()
s1 = student(*info)
info = input("Enter Name, Roll No, Gender, Seat No, Enrollment No, City : ").split()
s2 = student(*info)
"""
s = student()
s.set_details(name,roll_no,gender,seat_no,enroll_no,city)
s.get_details()