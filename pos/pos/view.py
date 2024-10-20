from django.shortcuts import render
from .models import Item, Receipt, History
from .forms import ProductItemForm
from .values import Items, CurrentCart
from django.shortcuts import redirect



# figure out how to limit the number of items in the cart because of quantity stock
def pos(request):
    print(Items)
    return render(request, 'POS.html', { 'items' : Items })

def add_item(request):
    if request.method == 'POST':
        item = ProductItemForm(request.POST, request.FILES)
        if item.is_valid():
            item.save()
            
            return redirect('/')
    else:
        item = ProductItemForm()    
    return render(request, 'AddItem.html', { 'form' : item })