class Rectangle:
    def __init__(self, l, b):
        self.l = len
        self.b = b
    def area(self):
        return self.l*self.b
    def parameter(self):
        return 2*(self.l+self.b)
r1 = Rectangle(5, 4)
r2 = Rectangle(6, 7)
print(r1.area())
print(r2.peremeter())


