class Bank:
    def __init__(self, bal):
        self.bal = bal
    def deposit(self):
        amt=float(input("enter the amount to be deposited :"))
        self.bal = self.bal+amt
        print("balance :", self.bal)
        return self.bal
    def withdrow(self):
        amt = float(input("enter the amount to be withdrow : "))
        if amt>self.bal:
            print("insufficent balance")
        else:
            b1.bal = b1.bal-amt
            print("balance :",b1.bal)
        return b1.bal
b1=Bank(0)
b2=Bank(0)
b1.deposit()
b2.withdrow()




