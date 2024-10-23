from .models import Item, Receipt, OrderItem

Items: list[Item] = []
CurrentCart: list[OrderItem] = []
Receipts: list[Receipt] = []