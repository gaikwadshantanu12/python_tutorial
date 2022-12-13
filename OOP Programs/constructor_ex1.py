class student:
    def __init__(self,name=None,roll=None,gender=None,seat_no=None,enroll_no=None,city=None):
        self.name = name
        self.roll_no = roll
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

name = input("Enter Name : ")
roll_no = int(input("Enter Roll No : "))
gender = input("Enter Gender : ")
seat_no = int(input("Enter Seat No : "))
enroll_no = int(input("Enter Enrollment No : "))
city = input("Enter City : ")

s1 = student(name,roll_no,gender,seat_no,enroll_no,city)
s2 = student()
s1.get_details()
s2.get_details()