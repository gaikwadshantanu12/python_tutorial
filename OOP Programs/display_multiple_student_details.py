#  WAP to print details of multiple students

class student:
    def set_details(self,name,roll_no,gender,seat_no,enroll_no,city):
        self.name = name
        self.roll_no = int(roll_no)
        self.gender = gender
        self.seat_no = int(seat_no)
        self.enroll_no = int(enroll_no)
        self.city = city

    def get_details(self):
        """print("\n\nName             :",self.name)
        print("Roll No          :", self.roll_no)
        print("Gender           :", self.gender)
        print("Seat No          :", self.seat_no)
        print("Enrollment No    :", self.enroll_no)
        print("City             :", self.city)"""
        print(f"|\t{self.name}\t|\t{self.roll_no}\t\t|\t{self.gender}\t|\t{self.seat_no}\t|\t{self.enroll_no}\t\t|\t{self.city}\t|")

arr = []
for i in range(10):
    s = student() # creating new object
    info = input("Enter Name, Roll No, Gender, Seat No, Enrollment No, City : ").split()
    s.set_details(*info)
    arr.append(s)

# Printing Details
print("\nList Of Students :\n")
print("-------------------------------------------------------------------------------------")
print("|\tName\t\t|\tRoll No\t|\tGender\t|\tSeat No\t|\tEnrollment No\t|\tCity\t|")
print("----------------|-----------|-----------|-----------|-------------------|-----------|")
for s in arr:
    s.get_details()
print("-------------------------------------------------------------------------------------")