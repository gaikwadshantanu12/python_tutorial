class A:
    def __init__(self, x):
        self.x = x
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x

class B:
    def __init__(self,y):
        self.y = y
    def setY(self,y):
        self.y = y
    def getY(self):
        return self.y

class C:
    def __init__(self,z):
        self.z = z
    def setZ(self,z):
        self.z = z
    def getZ(self):
        return self.z

class D(A,B,C):
    def __init__(self,x,y,z):
        A.__init__(self,x)
        B.__init__(self,y)
        C.__init__(self,z)
    def printXYZ(self):
        print(f"X : {self.getX()} \nY : {self.getY()} \nZ : {self.getZ()}")

d = D(10,20,30)
d.printXYZ()