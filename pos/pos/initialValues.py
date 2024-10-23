from .values import Items, Receipts
from .models import Item, OrderItem, Receipt

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
        "date": "2024-08-03",
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
        "date": "2024-08-06",
        "items": [
            {"name": "Grapes", "quantity": 3, "price": 75, "totalPrice": 252}
        ],
        "totalSub": 225,
        "totalTax": 27,
        "total_cost": 252
    },
    {
        "order_id": 10003,
        "date": "2024-08-10",
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
        "date": "2024-08-12",
        "items": [
            {"name": "Banana", "quantity": 5, "price": 60, "totalPrice": 324}
        ],
        "totalSub": 300,
        "totalTax": 36,
        "total_cost": 336
    },
    {
        "order_id": 10005,
        "date": "2024-08-15",
        "items": [
            {"name": "Apple", "quantity": 4, "price": 30, "totalPrice": 135.6}
        ],
        "totalSub": 120,
        "totalTax": 14.4,
        "total_cost": 134.4
    },
    {
        "order_id": 10006,
        "date": "2024-08-18",
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
        "date": "2024-08-20",
        "items": [
            {"name": "Banana", "quantity": 6, "price": 60, "totalPrice": 388.8}
        ],
        "totalSub": 360,
        "totalTax": 43.2,
        "total_cost": 403.2
    },
    {
        "order_id": 10008,
        "date": "2024-08-25",
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
        "date": "2024-08-28",
        "items": [
            {"name": "Apple", "quantity": 3, "price": 30, "totalPrice": 100.8}
        ],
        "totalSub": 90,
        "totalTax": 10.8,
        "total_cost": 100.8
    },
    {
        "order_id": 10010,
        "date": "2024-08-30",
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
        "date": "2024-09-04",
        "items": [
            {"name": "Pineapple", "quantity": 1, "price": 50, "totalPrice": 56}
        ],
        "totalSub": 50,
        "totalTax": 6,
        "total_cost": 56
    },
    {
        "order_id": 10012,
        "date": "2024-09-09",
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
        "date": "2024-09-10",
        "items": [
            {"name": "Apple", "quantity": 3, "price": 30, "totalPrice": 100.8}
        ],
        "totalSub": 90,
        "totalTax": 10.8,
        "total_cost": 100.8
    },
    {
        "order_id": 10014,
        "date": "2024-09-12",
        "items": [
            {"name": "Grapes", "quantity": 2, "price": 75, "totalPrice": 168},
            {"name": "Banana", "quantity": 1, "price": 60, "totalPrice": 67.2}
        ],
        "totalSub": 225,
        "totalTax": 27,
        "total_cost": 252
    },
    {
        "order_id": 10015,
        "date": "2024-09-15",
        "items": [
            {"name": "Apple", "quantity": 4, "price": 30, "totalPrice": 135.6}
        ],
        "totalSub": 120,
        "totalTax": 14.4,
        "total_cost": 135.6
    },
    {
        "order_id": 10016,
        "date": "2024-09-17",
        "items": [
            {"name": "Banana", "quantity": 2, "price": 60, "totalPrice": 134.4},
            {"name": "Orange", "quantity": 1, "price": 50, "totalPrice": 56}
        ],
        "totalSub": 190.4,
        "totalTax": 22.848,
        "total_cost": 213.248
    },
    {
        "order_id": 10017,
        "date": "2024-09-20",
        "items": [
            {"name": "Grapes", "quantity": 1, "price": 75, "totalPrice": 84}
        ],
        "totalSub": 75,
        "totalTax": 9,
        "total_cost": 84
    },
    {
        "order_id": 10018,
        "date": "2024-09-24",
        "items": [
            {"name": "Pineapple", "quantity": 3, "price": 50, "totalPrice": 168},
            {"name": "Banana", "quantity": 1, "price": 60, "totalPrice": 67.2}
        ],
        "totalSub": 225,
        "totalTax": 27,
        "total_cost": 252
    },
    {
        "order_id": 10019,
        "date": "2024-09-28",
        "items": [
            {"name": "Apple", "quantity": 5, "price": 30, "totalPrice": 168},
            {"name": "Orange", "quantity": 2, "price": 50, "totalPrice": 112}
        ],
        "totalSub": 280,
        "totalTax": 33.6,
        "total_cost": 313.6
    },
    {
        "order_id": 10020,
        "date": "2024-09-30",
        "items": [
            {"name": "Grapes", "quantity": 4, "price": 75, "totalPrice": 336}
        ],
        "totalSub": 300,
        "totalTax": 36,
        "total_cost": 336
    },

    # October Receipts
    {
        "order_id": 10021,
        "date": "2024-10-02",
        "items": [
            {"name": "Banana", "quantity": 4, "price": 60, "totalPrice": 268.8}
        ],
        "totalSub": 240,
        "totalTax": 28.8,
        "total_cost": 268.8
    },
    {
        "order_id": 10022,
        "date": "2024-10-12",
        "items": [
            {"name": "Apple", "quantity": 3, "price": 30, "totalPrice": 100.8},
            {"name": "Grapes", "quantity": 1, "price": 75, "totalPrice": 84}
        ],
        "totalSub": 165,
        "totalTax": 19.8,
        "total_cost": 184.8
    },
    {
        "order_id": 10023,
        "date": "2024-10-15",
        "items": [
            {"name": "Pineapple", "quantity": 2, "price": 50, "totalPrice": 112},
            {"name": "Apple", "quantity": 3, "price": 30, "totalPrice": 100.8}
        ],
        "totalSub": 212,
        "totalTax": 25.44,
        "total_cost": 237.44
    },
    {
        "order_id": 10024,
        "date": "2024-10-18",
        "items": [
            {"name": "Banana", "quantity": 6, "price": 60, "totalPrice": 402.24}
        ],
        "totalSub": 360,
        "totalTax": 43.2,
        "total_cost": 403.2
    },
    {
        "order_id": 10025,
        "date": "2024-10-20",
        "items": [
            {"name": "Grapes", "quantity": 5, "price": 75, "totalPrice": 420}
        ],
        "totalSub": 375,
        "totalTax": 45,
        "total_cost": 420
    },
    {
        "order_id": 10026,
        "date": "2024-10-21",
        "items": [
            {"name": "Pineapple", "quantity": 3, "price": 50, "totalPrice": 168},
            {"name": "Apple", "quantity": 4, "price": 30, "totalPrice": 135.6}
        ],
        "totalSub": 303.6,
        "totalTax": 36.43,
        "total_cost": 340.03
    },
    {
        "order_id": 10027,
        "date": "2024-10-22",
        "items": [
            {"name": "Orange", "quantity": 3, "price": 50, "totalPrice": 168},
            {"name": "Grapes", "quantity": 1, "price": 75, "totalPrice": 84}
        ],
        "totalSub": 252,
        "totalTax": 30.24,
        "total_cost": 282.24
    },
    {
        "order_id": 10028,
        "date": "2024-10-24",
        "items": [
            {"name": "Apple", "quantity": 4, "price": 30, "totalPrice": 135.6},
            {"name": "Pineapple", "quantity": 2, "price": 50, "totalPrice": 112}
        ],
        "totalSub": 247.6,
        "totalTax": 29.71,
        "total_cost": 277.31
    },
    {
        "order_id": 10029,
        "date": "2024-10-29",
        "items": [
            {"name": "Banana", "quantity": 2, "price": 60, "totalPrice": 134.4}
        ],
        "totalSub": 120,
        "totalTax": 14.4,
        "total_cost": 134.4
    },
    {
        "order_id": 10030,
        "date": "2024-10-30",
        "items": [
            {"name": "Grapes", "quantity": 2, "price": 75, "totalPrice": 168},
            {"name": "Orange", "quantity": 1, "price": 50, "totalPrice": 56}
        ],
        "totalSub": 224,
        "totalTax": 26.88,
        "total_cost": 250.88
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
    