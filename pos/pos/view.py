from django.shortcuts import render
from .models import Item, Receipt, History
from .forms import ProductItemForm, EditProductItemForm
from .values import Items, CurrentCart
from django.shortcuts import redirect



# figure out how to limit the number of items in the cart because of quantity stock
def pos(request):
    print(Items)
    return render(request, 'POS.html', { 'items' : Items })

def add_item(request):
    print(request.FILES)
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
    