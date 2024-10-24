from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import EditProductItemForm, ProductItemForm
from .functions import handlePOSActions
from .initialValues import getInitialValues
from .models import Item, OrderItem, Receipt
from .values import CurrentCart, Items, Receipts

getInitialValues()

# figure out how to limit the number of items in the cart because of quantity stock
def pos(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'checkout':
            totalSub = request.POST.get('totalSub')
            totalTax = request.POST.get('totalTax')
            totalPayment = request.POST.get('totalPayment')
            customerPayment = request.POST.get('customer-payment')

            if not customerPayment:
                print('no customer payment')
                return redirect('/')

            # creating a receipt
            receipt = Receipt(len(Receipts) + 1, float(totalTax), float(totalSub))

            for item in CurrentCart:
                receipt.add_item(item)
            Receipts.append(receipt)

            for item in Items:
                item.quantity = 0

            change = float(customerPayment) - float(totalPayment)

            Payments = {
                'totalPayment' : totalPayment,
                'totalSub' : totalSub,
                'totalTax' : totalTax,
                'customerPayment' : customerPayment,
                'change' : change
            }

            return render(request, 'POS.html', { 'items' : Items, 'Cart' : CurrentCart, 'Payments' : 
            Payments, 'Receipts' : receipt })
        elif action == 'decrement' or action == 'increment' or action == 'add':
            handlePOSActions(request.POST)
        elif action == 'clear':
            CurrentCart.clear()

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

def history(request):
    page = request.GET.get('page', 1)
    reciepts = [reciepts for idx, reciepts in enumerate(Receipts) if idx < int(page) * 10 and idx >= (int(page) - 1) * 10]
    search = None
    date = None
    if request.method == 'POST':
        search = request.POST.get('order_id')
        date = request.POST.get('date')
        page = 1 # page is always 1 when searching 

        if search:
            reciepts = [reciepts for idx, reciepts in enumerate(Receipts) 
                        if str(search) in str(reciepts.order_id) and idx <= int(page) * 10]
        elif date:
            reciepts = [reciepts for idx, reciepts in enumerate(Receipts) 
                        if str(date) in str(reciepts.date) and idx <= int(page) * 10]

    return render(request, 'history.html', { 'Receipts' : reciepts, 'search' : search, 'date' : date})