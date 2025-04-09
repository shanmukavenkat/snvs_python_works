class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_saved = price -deal_price
    def display_product_details(self):
        print("product Name: {}".format(self.name))
        print("product price: {}".format(self.price))
        print("product deal price: {}".format(self.deal_price))
        print("product rating: {}".format(self.rating))
        print("product you save: {}".format(self.you_saved))
    def get_deal_price(self):
        return self.deal_price
class ElectronincItem(Product):
    ##method overriding
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warranty_in_months = warranty_in_months
    def display_product_details(self):
        super().display_product_details()
        print("warranty: {}".format(self.warranty_in_months))

class Grocery(Product):
    ##method overriding
    def __init__(self,name,price,deal_price,rating,Expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.Expiry_date = Expiry_date
    def display_product_details(self):
        super().display_product_details()
        print("Expiry: {}".format(self.Expiry_date))


class Order:
    delivery_charges ={
        "normal":0,
        "prime Delivery":100
    }
    def __init__(self,delivery_method,delivery_address):
        self.delivery_method = delivery_method
        self.items = []
        self.delivery_address = delivery_address
    def add_items(self,product,quantity):
        item = (product,quantity)
        self.items.append(item)
    def display_order_details(self) -> object:
        print("Delivery Method : {}".format(self.delivery_method))
        print("Delivery Address : {}".format(self.delivery_address))
        print("---------------------------------------------------------------")
        for product,quantity in self.items:
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("")
            print("---------------------------------------------------------------")

        def get_total_bill(self):
            total_bill = 0
            for product,quantity in self.items:
                total_bill += product.get_deal_price()*quantity

            order_delivery_charges = Order.delivery_charges[self.delivery_method]
            total_bill += order_delivery_charges
            return total_bill

@classmethod
def update_delivery_charges(cls,delivery_method,delivery_charges):
    cls.delivery_charges[delivery_method] = delivery_charges


Tv = ElectronincItem("Tv",10000,8000,4.5,12)
Tv.display_product_details()
milk = Grocery("milk",50,40,4.5,"12/12/2020")
milk.display_product_details()


my_order = Order("normal","Bangalore")
my_order.add_items(Tv,2)
my_order.add_items(milk,3)
my_order.display_order_details()
Order.update_delivery_charges("normal",50)
my_order.display_order_details()
