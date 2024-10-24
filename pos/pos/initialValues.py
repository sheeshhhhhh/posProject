from .values import Items, Receipts
from .models import Item, OrderItem, Receipt
from datetime import datetime

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

receipts_data = [
    # August Receipts
    {
        "order_id": 10001,
        "date": datetime.strptime("2024-08-03", "%Y-%m-%d"),
        "items": [
            {"name": "Apple", "quantity": 2, "price": 30, "totalPrice": 67.2},
            {"name": "Banana", "quantity": 1, "price": 60, "totalPrice": 67.2}
        ],
        "totalSub": 120,
        "totalTax": 14.4,
        "total_cost": 134.4
    },
    {
        "order_id": 10002,
        "date": datetime.strptime("2024-08-06", "%Y-%m-%d"),
        "items": [
            {"name": "Grapes", "quantity": 3, "price": 75, "totalPrice": 252}
        ],
        "totalSub": 225,
        "totalTax": 27,
        "total_cost": 252
    },
    {
        "order_id": 10003,
        "date": datetime.strptime("2024-08-10", "%Y-%m-%d"),
        "items": [
            {"name": "Orange", "quantity": 2, "price": 50, "totalPrice": 112},
            {"name": "Pineapple", "quantity": 1, "price": 50, "totalPrice": 56}
        ],
        "totalSub": 168,
        "totalTax": 20.16,
        "total_cost": 188.16
    },
    {
        "order_id": 10004,
        "date": datetime.strptime("2024-08-12", "%Y-%m-%d"),
        "items": [
            {"name": "Banana", "quantity": 5, "price": 60, "totalPrice": 324}
        ],
        "totalSub": 300,
        "totalTax": 36,
        "total_cost": 336
    },
    {
        "order_id": 10005,
        "date": datetime.strptime("2024-08-15", "%Y-%m-%d"),
        "items": [
            {"name": "Apple", "quantity": 4, "price": 30, "totalPrice": 135.6}
        ],
        "totalSub": 120,
        "totalTax": 14.4,
        "total_cost": 134.4
    },
    {
        "order_id": 10006,
        "date": datetime.strptime("2024-08-18", "%Y-%m-%d"),
        "items": [
            {"name": "Grapes", "quantity": 2, "price": 75, "totalPrice": 168},
            {"name": "Orange", "quantity": 3, "price": 50, "totalPrice": 168}
        ],
        "totalSub": 336,
        "totalTax": 40.32,
        "total_cost": 376.32
    },
    {
        "order_id": 10007,
        "date": datetime.strptime("2024-08-20", "%Y-%m-%d"),
        "items": [
            {"name": "Banana", "quantity": 6, "price": 60, "totalPrice": 388.8}
        ],
        "totalSub": 360,
        "totalTax": 43.2,
        "total_cost": 403.2
    },
    {
        "order_id": 10008,
        "date": datetime.strptime("2024-08-25", "%Y-%m-%d"),
        "items": [
            {"name": "Pineapple", "quantity": 2, "price": 50, "totalPrice": 112},
            {"name": "Grapes", "quantity": 1, "price": 75, "totalPrice": 84}
        ],
        "totalSub": 196,
        "totalTax": 23.52,
        "total_cost": 219.52
    },
    {
        "order_id": 10009,
        "date": datetime.strptime("2024-08-28", "%Y-%m-%d"),
        "items": [
            {"name": "Apple", "quantity": 3, "price": 30, "totalPrice": 100.8}
        ],
        "totalSub": 90,
        "totalTax": 10.8,
        "total_cost": 100.8
    },
    {
        "order_id": 10010,
        "date": datetime.strptime("2024-08-30", "%Y-%m-%d"),
        "items": [
            {"name": "Orange", "quantity": 5, "price": 50, "totalPrice": 280},
            {"name": "Banana", "quantity": 2, "price": 60, "totalPrice": 134.4}
        ],
        "totalSub": 414,
        "totalTax": 49.68,
        "total_cost": 463.68
    },

    # September Receipts
    {
        "order_id": 10011,
        "date": datetime.strptime("2024-09-04", "%Y-%m-%d"),
        "items": [
            {"name": "Pineapple", "quantity": 1, "price": 50, "totalPrice": 56}
        ],
        "totalSub": 50,
        "totalTax": 6,
        "total_cost": 56
    },
    {
        "order_id": 10012,
        "date": datetime.strptime("2024-09-09", "%Y-%m-%d"),
        "items": [
            {"name": "Orange", "quantity": 2, "price": 50, "totalPrice": 112},
            {"name": "Banana", "quantity": 1, "price": 60, "totalPrice": 67.2}
        ],
        "totalSub": 160,
        "totalTax": 19.2,
        "total_cost": 179.2
    },
    {
        "order_id": 10013,
        "date": datetime.strptime("2024-09-15", "%Y-%m-%d"),
        "items": [
            {"name": "Apple", "quantity": 1, "price": 30, "totalPrice": 33.6}
        ],
        "totalSub": 30,
        "totalTax": 3.6,
        "total_cost": 33.6
    },
    {
        "order_id": 10014,
        "date": datetime.strptime("2024-09-20", "%Y-%m-%d"),
        "items": [
            {"name": "Banana", "quantity": 2, "price": 60, "totalPrice": 134.4}
        ],
        "totalSub": 120,
        "totalTax": 14.4,
        "total_cost": 134.4
    },
    {
        "order_id": 10015,
        "date": datetime.strptime("2024-09-25", "%Y-%m-%d"),
        "items": [
            {"name": "Grapes", "quantity": 3, "price": 75, "totalPrice": 252}
        ],
        "totalSub": 225,
        "totalTax": 27,
        "total_cost": 252
    },
    {
        "order_id": 10016,
        "date": datetime.strptime("2024-09-30", "%Y-%m-%d"),
        "items": [
            {"name": "Orange", "quantity": 2, "price": 50, "totalPrice": 112},
            {"name": "Pineapple", "quantity": 1, "price": 50, "totalPrice": 56}
        ],
        "totalSub": 168,
        "totalTax": 20.16,
        "total_cost": 188.16
    },

    # October Receipts
    {
        "order_id": 10017,
        "date": datetime.strptime("2024-10-01", "%Y-%m-%d"),
        "items": [
            {"name": "Grapes", "quantity": 1, "price": 75, "totalPrice": 84}
        ],
        "totalSub": 75,
        "totalTax": 9,
        "total_cost": 84
    },
    {
        "order_id": 10018,
        "date": datetime.strptime("2024-10-05", "%Y-%m-%d"),
        "items": [
            {"name": "Apple", "quantity": 4, "price": 30, "totalPrice": 135.6}
        ],
        "totalSub": 120,
        "totalTax": 14.4,
        "total_cost": 134.4
    },
    {
        "order_id": 10019,
        "date": datetime.strptime("2024-10-10", "%Y-%m-%d"),
        "items": [
            {"name": "Banana", "quantity": 6, "price": 60, "totalPrice": 388.8}
        ],
        "totalSub": 360,
        "totalTax": 43.2,
        "total_cost": 403.2
    },
    {
        "order_id": 10020,
        "date": datetime.strptime("2024-10-15", "%Y-%m-%d"),
        "items": [
            {"name": "Pineapple", "quantity": 1, "price": 50, "totalPrice": 56}
        ],
        "totalSub": 50,
        "totalTax": 6,
        "total_cost": 56
    },
    {
        "order_id": 10021,
        "date": datetime.strptime("2024-10-20", "%Y-%m-%d"),
        "items": [
            {"name": "Grapes", "quantity": 2, "price": 75, "totalPrice": 168},
            {"name": "Orange", "quantity": 3, "price": 50, "totalPrice": 168}
        ],
        "totalSub": 336,
        "totalTax": 40.32,
        "total_cost": 376.32
    },
    {
        "order_id": 10022,
        "date": datetime.strptime("2024-10-25", "%Y-%m-%d"),
        "items": [
            {"name": "Banana", "quantity": 1, "price": 60, "totalPrice": 67.2}
        ],
        "totalSub": 60,
        "totalTax": 7.2,
        "total_cost": 67.2
    },
    {
        "order_id": 10023,
        "date": datetime.strptime("2024-10-30", "%Y-%m-%d"),
        "items": [
            {"name": "Apple", "quantity": 3, "price": 30, "totalPrice": 100.8}
        ],
        "totalSub": 90,
        "totalTax": 10.8,
        "total_cost": 100.8
    }
]

def getInitialValues():
        for data in item_data:
            item = Item(data["name"], data["Image"], data["price"], data["quantityInStock"], data["isAvailable"])
            item.itemId = generateId()
            Items.append(item)

        for order in receipts_data:
            # create Orderitem
            currentCart = []
            for data_item in order['items']:
                item_obj = next((item for item in Items if item.name == data_item["name"]), None)
                orderItem = OrderItem(item_obj, data_item['quantity'])
                currentCart.append(orderItem)
                
            # create Receipt
            receipt = Receipt(order["order_id"], order["totalTax"], order["totalSub"], order["date"])

            for item in currentCart:
                receipt.add_item(item)
            Receipts.append(receipt)
    