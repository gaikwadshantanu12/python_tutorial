class A:
    def __init__(self):
        super().__init__()
        self.x = 10
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20
    def setY(self,y):
        self.y = y
    def getY(self):
        return self.y

class C:
    def __init__(self):
        super().__init__()
        self.z = 30
    def setZ(self,z):
        self.z = z
    def getZ(self):
        return self.z

class D(B,C):
    def __init__(self):
        super().__init__()
    def printXYZ(self):
        print(f"X : {self.getX()} \nY : {self.getY()} \nZ : {self.getZ()}")

d = D()
d.printXYZ()

# super().__init()__ is necessary / compulsory in all classes