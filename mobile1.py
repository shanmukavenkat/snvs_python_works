class Mobile:
    def __init__(self,model,price):
        self.model = model
        self.pirce = price
    def make_call(self,number):
        print("calling......{}".format(number))
    def get_model(self):
        print(self.model)

obj = Mobile("nokia", 1000)
obj.get_model()
obj1 = Mobile("samsung", 2000)
obj1.get_model()
# In the above example, we have created two objects obj and obj1.
# Both the objects have different values for the instance variable model.
# But, the method get_model() is common for both the objects.
# So, we can define the method get_model() in the class and call it using both the objects.
# This is the advantage of using classes.