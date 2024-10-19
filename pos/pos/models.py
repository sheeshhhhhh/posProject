import datetime

class Item():
    def __init__(self, name, Image, price, quantity, isAvaialble):
        self.itemId = None #supposed to be random
        self.Image = Image
        self.name = name
        self.price = price
        self.quantity = quantity #this is how much is bought
        self.quantityInStock = 0 #and this is how much is in stock
        self.isAvaialble = isAvaialble
        self.Category = None #don't know if will be used

    def calculate_tax(self):
        # ano na to fix na yung 0.12 na tax di naman nababago yun eh
        return self.price * 0.12
        
    def calculate_total(self):
        return self.price + self.calculate_tax()

    def add_quantity(self, quantity):
        self.quantity += quantity

    def remove_quantity(self, quantity):
        self.quantity -= quantity

    def __str__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.isAvaialble})"

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.isAvaialble})"
        
class Receipt:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.calculate_total()
        return total_cost
    
    def __str__(self):
        return f"Receipt({self.order_id}, cost={self.calculate_total_cost()})"

    def __repr__(self):
        return f"Receipt({self.order_id}, cost={self.calculate_total_cost()})"
    

class History:
    def __init__(self, receipt: Receipt):
        self.receipt = receipt
        self.data = datetime.datetime.now()
