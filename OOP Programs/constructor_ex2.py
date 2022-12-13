# WAP to create rectangle

class rectangle:
    def __init__(self,length=0,width=0):
        self.length = length
        self.width = width

    def calculate_area(self):
        return (self.length * self.width)

    def calculate_perimeter(self):
        return (2 * (self.length + self.width))

l = int(input("Enter length of rectangle : "))
w = int(input("Enter width of rectangle : "))

r = rectangle(l,w)
print("Area of rectangle :",r.calculate_area())
print("Perimeter of rectangle :",r.calculate_perimeter())