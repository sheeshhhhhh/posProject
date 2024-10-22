from .values import Items
from .models import Item

def generateId():
        item_id = (len(Items) + 1) + 1
        return item_id

# the image should be uploaded to the media folder
item_data = [
    {
        "name": "Apple",
        "Image": "/media/uploads/apple.webp",
        "price": 30,
        "quantityInStock": 5,
        "isAvailable": True
    },
    {
        "name": "Banana",
        "Image": "/media/uploads/banana.jpg",
        "price": 60,
        "quantityInStock": 30,
        "isAvailable": True
    },
    {
        "name": "Orange",
        "Image": "/media/uploads/orange.jpg",
        "price": 50,
        "quantityInStock": 10,
        "isAvailable": True
    },
    {
        "name": "Grapes",
        "Image": "/media/uploads/grapes.jfif",
        "price": 75,
        "quantityInStock": 10,
        "isAvailable": True
    },
    {
        "name": "Pineapple",
        "Image": "/media/uploads/pineapple.webp",
        "price": 50.00,
        "quantityInStock": 10,
        "isAvailable": True
    },
]

def getInitialValues():
        for data in item_data:
            item = Item(data["name"], data["Image"], data["price"], data["quantityInStock"], data["isAvailable"])
            item.itemId = generateId()
            Items.append(item)