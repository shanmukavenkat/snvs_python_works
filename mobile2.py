class Mobile:
    def __init__(self,model,price):
        self.model = model
        self.pirce = price
    def make_call(self,number):
        print("calling......{}".format(number))
    def get_model(self):
        print(self.model)
    def update_model(self,model):
        self.model = model

obj = Mobile("nokia", 1000)
obj.get_model()
obj1 = Mobile("samsung", 2000)
obj1.get_model()
