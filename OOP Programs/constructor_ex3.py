# WAP to create circle
import math
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (math.pi * math.pow(self.radius,2))

    def circumference(self):
        return (2 * math.pi * self.radius)

r = eval(input("Enter radius of circle : "))
c = circle(r)
print("Area of circle :",c.area())
print("Circumference of circle :",c.circumference())