class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price-deal_price
    def display_product_details(self):
        print("product Name: {}".format(self.name))
        print("product price: {}".format(self.price))
        print("product deal price: {}".format(self.deal_price))
        print("product rating: {}".format(self.rating))
        print("product you save: {}".format(self.you_save))

class Electronic_item(Product):
    def set_warranty(self,warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months
    def display_electronic_product_details(self):
        self.display_product_details()
        print("warranty: {}".format(self.warranty_in_months))

class Grocery_item(Product):
    def set_expiry_date(self,expiry_date):
        self.expiry_date = expiry_date

e_item = Electronic_item("Mobile",10000,8000,4.5)
e_item.set_warranty(24)
print(e_item.get_warranty())
print("___----___----___----___----___ ")

g_item = Grocery_item("Rice",50,40,4.5)
g_item.display_product_details()
