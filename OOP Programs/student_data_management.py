class Student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    def get_roll(self):
        return self.roll
    def get_name(self):
        return self.name
    def get_marks(self):
        return self.marks
    def display_instance(self):
        print(f"Roll No : {self.roll}\n"
              f"Name    : {self.name}\n"
              f"Marks   : {self.marks}\n\n")
    def display(self):
        print(f"{self.roll:<6d}{self.name:30s}{self.marks:5.2f}")

std = []
while(1):
    print(f"1. Add Record\n"
          f"2. Search By Roll No\n"
          f"3. Search By Name\n"
          f"4. Delete Record\n"
          f"5. Display All\n"
          f"6. Display Merit List\n"
          f"0. Exit\n\n")
    choice = int(input("Enter the choice : "))

    if choice == 0:
        break

    elif choice == 1:
        roll = int(input("\nEnter Roll No : "))
        name = input("Enter Name : ")
        marks = float(input("Enter Percentage Marks : "))
        s = Student(roll,name.title(),marks)
        std.append(s)
        print("\nRecord Has Been Added Successfully !\n\n")

    elif choice == 2:
        roll = int(input("\n\nEnter Roll No To Search : "))
        flag = False
        for s in std:
            if s.get_roll() == roll:
                s.display_instance()
                flag = True
                break

        if flag == False:
            print(f"Roll No {roll} Not Found")

    elif choice == 3:
        name = input("\n\nEnter Name To Search : ")
        flag = False
        for s in std:
            if name.lower() in s.get_name().lower():
                s.display_instance()
                flag = True

        if not flag:
            print(f"{name} Not Found")

    elif choice == 4:
        roll = int(input("\n\nEnter Roll No To Delete : "))
        flag = False
        for s in std:
            if s.get_roll() == roll:
                d = s
                flag = True
                break

        if flag:
            std.remove(d)
            print("\nRecord Has Been Deleted")
        else:
            print(f"Roll No {roll} Not Found")

    elif choice == 5:
        print(f"{'Roll':6s}{'Name':30s}{'Marks':5s}")
        for s in std:
            s.display()

    elif choice == 6:
        merit = sorted(std,key=lambda s:s.get_marks(),reverse=True)
        print(f"{'Roll':6s}{'Name':30s}{'Marks':5s}")
        for s in merit:
            s.display()

    else:
        print("\nInvalid Choice")

    input("\n>>> Hit Enter To Continue >>>\n")

print("\nThank You")