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

class C(B):
    def __init__(self,x,y,z):
        super().__init__(x,y)       # B.__init__(self,x,y)
        self.z = z
    def setZ(self,z):
        self.z = z
    def getZ(self):
        return self.z
    def printXYZ(self):
        print("X :", self.x,", Y :", self.y,", Z :",self.z)

c = C(10,20,30)
print("Before :")
c.printXYZ()
c.setX(45)
c.setY(55)
c.setZ(65)
print("\nAfter :")
print("X :",c.getX(),", Y :",c.getY(),", Z :",c.getZ())
print("\n\n",dir(C))