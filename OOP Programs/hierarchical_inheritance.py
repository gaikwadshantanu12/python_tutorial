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
        print("X :",self.getX(),", Y :",self.getY())

class C(A):
    def __init__(self,x,z):
        super().__init__(x)       # A.__init__(self,x)
        self.z = z
    def setZ(self,z):
        self.z = z
    def getZ(self):
        return self.z
    def printXZ(self):
        print("X :",self.getX(),", Z :",self.getZ())

b = B(10,20)
c = C(50,60)
# print("B\'s Dictionary :",b.__dict__)
# print("C\'s Dictionary :",c.__dict__)
b.printXY()
c.printXZ()