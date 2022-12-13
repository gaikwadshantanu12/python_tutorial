class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def print_info(self):
        print(f"Name        : {self.name}\n"
              f"Age         : {self.age}\n"
              f"City        : {self.city}")

class Student(Person):
    def __init__(self,rollno,name,age,city,marks):
        super().__init__(name,age,city)
        self.rollno = rollno
        self.marks = marks
    def print_info(self):           # method overriding
        print(f"Roll No     : {self.rollno}")
        super().print_info()
        print(f"Marks       : {self.marks}\n\n")

class Employee(Person):
    def __init__(self,emp_id,name,age,city,salary):
        super().__init__(name,age,city)
        self.emp_id = emp_id
        self.salary = salary
    def print_info(self):
        print(f"EMP ID      : {self.emp_id}")
        super().print_info()
        print(f"Salary      : {self.salary}")

a = [Student(51,"Shantanu A. Gaikwad",20,"Buldana",95.80), Employee(101,"Shantanu Anant Gaikwad",20,"Buldana",100000)]
a[0].print_info()
a[1].print_info()
