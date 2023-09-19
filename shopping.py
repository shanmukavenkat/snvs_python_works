class Cart:
    #class attribute
    flat_discount = 0
    min_bill = 100
    def __init__(self):
        self.items = {}
    def add_items(self,item_name,quantity):
        self.items[item_name] = quantity
        self.display_items()
    def display_items(self):
        print(self.items)

    def print_bill(self):
        print(Cart.min_bill)

    @classmethod  ## we have to place decorator before class method
    def update_flat_discount(cls,new_flat_discount):
        cls.flat_discount = new_flat_discount

    @classmethod
    def increase_flat_discount(cls, amount):
        new_flat_discount = cls.flat_discount + amount
        cls.update_flat_discount(new_flat_discount)

    @staticmethod
    def greet():
        print("Have a great shopping day")






print("Staticmethod")
Cart.greet()
print("updated class value in methods")
print(Cart.flat_discount)
Cart.update_flat_discount(80)
print(Cart.flat_discount)
print("---------------------")
a = Cart()
b = Cart()
a.print_bill()
b.print_bill()
print("updated class value")
Cart.min_bill = 200
a.print_bill()
b.print_bill()
