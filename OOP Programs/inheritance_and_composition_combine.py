# IS A Relationship -> Inheritance
# HAS A Relationship -> Composition

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_per_info(self):
        print(f"Name        : {self.name}\n"
              f"Age         : {self.age}")

class Employee(Person):
    def __init__(self,uid,name,age,car):
        self.uid = uid
        super().__init__(name,age)      # Person.__init__(self,name,age)
        self.car = car      # Object of another class
    def print_emp_info(self):
        self.print_per_info()
        print(f"EMP_ID      : {self.uid}\n")
        self.car.print_car_info()

class Car:
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
    def print_car_info(self):
        print(f"Has Car :- \n"
              f"Make        : {self.make}\n"
              f"Model       : {self.model}\n"
              f"Color       : {self.color}\n")

e = Employee(123,"Ramesh",30,Car("Honda","WR-V","White"))
e.print_emp_info()