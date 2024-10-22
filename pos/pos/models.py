import datetime

class Item():
    def __init__(self, name, Image, price, quantity, isAvailable):
        self.itemId = None #supposed to be random
        self.Image = Image #this is the image url
        self.name = name
        self.price = price
        self.quantityInStock = quantity #and this is how much is in stock
        self.isAvailable = isAvailable
        self.totalPrice = self.calculate_total()

        self.quantity = 0

    def calculate_tax(self):
        # ano na to fix na yung 0.12 na tax di naman nababago yun eh
        return self.price * 0.12
        
    def calculate_total(self):
        return self.price + self.calculate_tax()

    def addStockQuantity(self, quantity):
        self.quantityInStock += quantity

    def removeStockQuantity(self, quantity):
        self.quantityInStock -= quantity

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class OrderItem:
    def __init__(self, item: Item, quantity: int):
        self.item = item
        self.quantity = quantity

    def calculate_total(self):
        return self.item.calculate_total() * self.quantity

    def __str__(self):
        return f"OrderItem({self.item}, quantity={self.quantity})"

    def __repr__(self):
        return f"OrderItem({self.item}, quantity={self.quantity})"

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
