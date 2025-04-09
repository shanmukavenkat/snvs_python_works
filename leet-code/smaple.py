class Store:
    def __init__(self):
        self.items ={ "Butter":10 ,"bread":30}
    def add_items(self,name,quantity):
      self.items[name]+= quantity
s = Store()
s.add_items(10)