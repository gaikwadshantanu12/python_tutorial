class Employee:
    def __init__(self,id,name,age,car):
        self.id = id
        self.name = name
        self.age = age
        self.car = car      # object of another class

    def print_emp_info(self):
        print(f"Emp_ID      : {self.id}\n"
              f"Name        : {self.name}\n"
              f"Age         : {self.age}\n")
        self.car.print_car_info()

class Car:
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color

    def print_car_info(self):
        print(f"Has Car\n"
              f"Make        : {self.make}\n"
              f"Model       : {self.model}\n"
              f"Color       : {self.color}")

car = Car("Honda","WR-V","White")
emp = Employee(101,"Shantanu Gaikwad",19,car)
emp.print_emp_info()