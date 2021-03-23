class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.l
    def peremeter(self):
        return 2*(self.l+self.b)
r1=Rectangle(4,5)
r2=Rectangle(9,2)
a1=r1.area()
a2=r2.area()
p1=r1.peremeter()
p2=r1.peremeter()
    if a1>a2:
        print("first object has bigger area than second object  ")
    else:
        print("second object has bigger area than frist object ")
    if p1>p2:
        print("first object has bigger peremeter than second object ")
    else:
        print("second object has bigger peremeter than first object ")



