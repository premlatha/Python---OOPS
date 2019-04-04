# Employee class
class employee:

    #Class variable - raise_amount
    raise_amount=1.04

    # Init method
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    def fullname(self):
        return self.first+' '+self.last

    def annaul_raise(self):
        self.pay=int(self.pay+employee.raise_amount)


emp1=employee('John','Smith',50000)
print(emp1.fullname())