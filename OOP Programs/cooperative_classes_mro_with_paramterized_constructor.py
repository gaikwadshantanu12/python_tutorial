class A:
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.x = kwargs['x']
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x

class B(A):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.y = kwargs['y']
    def setY(self,y):
        self.y = y
    def getY(self):
        return self.y

class C:
    def __init__(self,**kwargs):
        super().__init__()      # not necessary
        self.z = kwargs['z']
    def setZ(self,z):
        self.z = z
    def getZ(self):
        return self.z

class D(B,C):
    def __init__(self,**kwargs):        # variable length keyword arguments
        super().__init__(**kwargs)
    def printXYZ(self):
        print(f"X : {self.getX()} \nY : {self.getY()} \nZ : {self.getZ()}")

d = D(x=50,y=70,z=90)
d.printXYZ()