class Test:
    def __init__(self,m1,m2):
        self.m1 = 40
        self.m2 = 50


class Grade(Test):
    def __init__(self, tot):
        self.tot = tot
o = Grade()
o.tot = o.m1 + o.m2
print(o.tot)
