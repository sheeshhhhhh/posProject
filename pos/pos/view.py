from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import EditProductItemForm, ProductItemForm
from .functions import getMonthNumber, handlePOSActions, processDataDashboard
from .initialValues import getInitialValues
from .models import Item, OrderItem, Receipt
from .values import CurrentCart, Items, Receipts

getInitialValues()

def pos(request):
    items = Items
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
                if item.totalQuantity() <= 0:
                    item.isAvailable = False

            change = float(customerPayment) - float(totalPayment)

            Payments = {
                'totalPayment' : totalPayment,
                'totalSub' : totalSub,
                'totalTax' : totalTax,
                'customerPayment' : customerPayment,
                'change' : change
            }

            return render(request, 'POS.html', { 'items' : Items, 'Cart' : CurrentCart, 
                            'Payments' : Payments, 'Receipts' : receipt })
        elif action == 'decrement' or action == 'increment' or action == 'add':
            handlePOSActions(request.POST)
        elif action == 'clear':
            CurrentCart.clear()


    search = request.GET.get('search') or ''
    
    if search:
        items = [item for item in Items if search.lower() in item.name.lower() or search in str(item.itemId)]

    Payments = {
        'totalPayment' : 0,
        'totalSub' : 0,
        'totalTax' : 0,
    }
    
    for item in CurrentCart:
        Payments['totalPayment'] += item.calculate_total() 
        Payments['totalSub'] += item.item.price * item.quantity
        Payments['totalTax'] +=  item.item.calculate_tax() * item.quantity
        
    return render(request, 'POS.html', { 'items' : items, 'Cart' : CurrentCart, 'Payments' : Payments, 'search' : search })

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

    return render(request, "ViewtoEdit.html", { 'items' : Items})

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
    page_number = int(request.GET.get('page', 1) or 1)
    item_per_page = 10

    search = request.GET.get('order_id', '') or ''
    date_str  = request.GET.get('date')



    filtered_receipts = Receipts

    if search:
        filtered_receipts = [receipt for receipt in Receipts if search in str(receipt.order_id)]

    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            filtered_receipts = [receipt for receipt in Receipts if date == receipt.date.date()]
        except ValueError as e:
            print(e)
            date = None 

    start_index = (page_number - 1) * item_per_page
    end_index = start_index + item_per_page
    paginated_receipts = filtered_receipts[start_index:end_index]

    # check for pagination avalailable
    has_next = end_index < len(filtered_receipts)
    has_previous = start_index > 0

    return render(request, 'history.html', { 
        'Receipts' : paginated_receipts, 
        'search' : search, 
        'date' : date_str,
        'page_number': page_number,
        'has_next': has_next,
        'has_previous': has_previous
    })

def dashboard(request):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return render(request, 'Dashboard.html', { 'months' : months })

@require_http_methods(['GET'])
def api_dashboard(request):
    month = request.GET.get('month')
    getMonthNum = getMonthNumber(month)
    data = None

    if getMonthNum is None:
        return JsonResponse({'error' : 'Month not found'}, status=404)
    else:
        data = processDataDashboard(getMonthNum)

    return JsonResponse(data, status=200)
