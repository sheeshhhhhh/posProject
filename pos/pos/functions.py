
from django.shortcuts import redirect

from .models import OrderItem
from .values import CurrentCart, Items


# POS ACTIONS WILL INCLUDE INCREMENT, DECREMENT AND ADD(OR EDIT)
# body represents the request.POST
def handlePOSActions(body):
    item_id = body.get('item_id')
    quantity = body.get('quantity')
    if not quantity:
        quantity = 0 
    else:
        quantity = int(quantity)
    action = body.get('action')

    #https://www.geeksforgeeks.org/python-list-comprehension/ #Conditional statements in list comprehension
    item = next((item for item in Items if item.itemId == int(item_id)), None)

    if item is None:
        return redirect('/error')
    
    if action == 'increment':
        quantity += 1
        
        if item.totalQuantity() == 0 or item.totalQuantity() < quantity:
            return redirect('/')
        
        item.quantityInStock = item.totalQuantity() - quantity
        item.quantity = quantity
    elif action == 'decrement':
        quantity -= 1
        if quantity < 0:
            return redirect('/')
        
        item.quantityInStock = item.totalQuantity() - quantity
        item.quantity = quantity
    elif action == 'add':
        if item.totalQuantity() < quantity or quantity < 0:
            return redirect('/')
     
        item.quantityInStock = item.totalQuantity() - quantity
        item.quantity = quantity

    cart_item = next((cartItem for cartItem in CurrentCart if cartItem.item.itemId == int(item_id)), None)
    if cart_item:
        cart_item.quantity = quantity
    else:
        cart_item = OrderItem(item, quantity)
        CurrentCart.append(cart_item)

    # cleaning the cart if 0 na yung quantity
    for cartItem in CurrentCart:
        if cartItem.quantity == 0:
            CurrentCart.remove(cartItem)
