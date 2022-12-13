class A:
    def __init__(self, x):
        self.x = x
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x

class B(A):
    def __init__(self,x,y):
        super().__init__(x)     # A.__init__(self,x)
        self.y = y
    def setY(self,y):
        self.y = y
    def getY(self):
        return self.y
    def printXY(self):
        print("X :", self.x, ", Y :", self.y)

b = B(10,20)
print("Before :")
b.printXY()
b.setX(45)
b.setY(70)
print("\nAfter :")
print("X :",b.getX(),", Y :",b.getY())