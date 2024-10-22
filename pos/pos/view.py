from django.shortcuts import redirect, render

from .forms import EditProductItemForm, ProductItemForm
from .initialValues import getInitialValues
from .models import History, Item, OrderItem, Receipt
from .values import CurrentCart, Items

getInitialValues()

# figure out how to limit the number of items in the cart because of quantity stock
def pos(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        action = request.POST.get('action')

        item = next((item for item in Items if item.itemId == int(item_id)), None)

        if item is None:
            return redirect('/error')

        if item.quantityInStock == 0 and action == 'add':
            return redirect('/error')

        if action == 'increment':
            quantity += 1
            item.quantityInStock -= 1
        elif action == 'decrement':
            quantity -= 1
            item.quantityInStock += 1
        item.quantity = quantity
        
        cart_item = next((cartItem for cartItem in CurrentCart if cartItem.item.itemId == int(item_id)), None)

        if cart_item:
            cart_item.quantity = quantity
        else:
            cart_item = OrderItem(item, quantity)
            CurrentCart.append(cart_item)

    print(CurrentCart)

    Payments = {
        'totalPayment' : 0,
        'totalSub' : 0,
        'totalTax' : 0,
    }
    
    for item in CurrentCart:
        Payments['totalPayment'] += item.calculate_total() 
        Payments['totalSub'] += item.item.price * item.quantity
        Payments['totalTax'] +=  item.item.calculate_tax() * item.quantity
        
    return render(request, 'POS.html', { 'items' : Items, 'Cart' : CurrentCart, 'Payments' : Payments })

def add_item(request):
    if request.method == 'POST':
        item = ProductItemForm(request.POST, request.FILES)
        if item.is_valid():
            item.save()

            return redirect('/')
    else:
        item = ProductItemForm()    
    return render(request, 'AddItem.html', { 'form' : item })

def ViewItemToEdit(request):

    return render(request, "ViewToEdit.html", { 'items' : Items})

#id is slug
# reference https://www.w3schools.com/django/django_slug_field.php on Modify View Section
def edit_item(request, id):


    if request.method == 'POST':
        initialImage = None
        for item in Items:
            if item.itemId == int(id):
                initialImage = item.Image    
                break

        item = EditProductItemForm(request.POST, request.FILES, initial={
            'Image' :  initialImage
        })
        if item.is_valid():
            # shoud put item.editSave() here later
            item.save()
            return redirect('/')            
    else:
        for item in Items:
            if item.itemId == int(id):
                initial = {
                    'id' : item.itemId,
                    'name': item.name,
                    'price': item.price,
                    'quantityInStock': item.quantityInStock,
                    'isAvailable': item.isAvailable,
                    'Image': item.Image,
                }
                item = EditProductItemForm(initial=initial)
                break
        
        if initial == None:
            return redirect('/error')
    
    return render(request, 'EditItem.html', { 'form' : item })
    