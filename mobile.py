class moblie:
    def __init__(self,model,price):
        self.model = model
        self.pirce = price
    def make_call(self,number):
        print("calling......{}".format(number))

obj = moblie("nokia",1000)
obj.make_call(1234567890)
obj1= moblie("samsung",2000)
obj1.make_call(1234567890)