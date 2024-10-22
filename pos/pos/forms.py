from random import seed

from django import forms
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage, default_storage

from .models import Item
from .values import CurrentCart, Items

#all of this is not tested

class ProductItemForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the name of the item',
            'class': 'w-full h-[40px] text-xl font-medium px-2 outline-none border-2 rounded-lg',  # Add any additional classes here
        }),
    )
    price = forms.FloatField(
        label='Price',
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'onkeydown': "return event.keyCode !== 69",
            'class': 'max-w-[120px] h-[40px] text-xl font-medium px-2 outline-none',
        }),
    )
    quantityInStock = forms.IntegerField(
        label='Quantity',
        required=True,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'onkeydown': "return event.keyCode !== 69",
            'class': 'max-w-[120px] h-[40px] text-xl font-medium px-2 outline-none border-2 rounded-lg',
        }),
    )
    isAvailable = forms.BooleanField(
        label='Is Available',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-[25px] h-[25px] ml-3',
        }),
    )
    Image = forms.ImageField(
        label='Image',
        required=True,
    )
    #category = forms.CharField(label='Category', max_length=100)


    def generateId(self):
        item_id = (len(Items) + 1) + 1
        return item_id
            
    def clean(self):
        cleaned_data = super().clean()

        #check in the array if the name already exists
        for item in Items:
            if cleaned_data.get('name') == item.name:
                self.add_error('name', 'Name already exists')

        if cleaned_data.get('price') <= 0: 
            self.add_error('price', 'Price cannot be 0 or negative')

        if cleaned_data.get('Image') == None:
            self.add_error('Image', 'Image is required')

        if cleaned_data.get('quantityInStock') < 0:
            self.add_error('quantityInStock', 'Quantity cannot be negative')

        if cleaned_data.get('isAvailable') == True and cleaned_data.get('quantityInStock') <= 0:
            self.add_error('isAvailable', 'Item cannot be available if there is no stock')

        return cleaned_data

    def save(self):
        cleaned_data = self.clean()

        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        quantityInStock = cleaned_data.get('quantityInStock')
        isAvailable = cleaned_data.get('isAvailable')
        ImageFile = cleaned_data.get('Image')

        #saving the image
        fs = FileSystemStorage()
        
        media_path = default_storage.save('uploads/' + ImageFile.name, ContentFile(ImageFile.read()))
        filename = fs.save(media_path, ImageFile)
        uploadedFileUrl = fs.url(filename)

        item = Item(name, uploadedFileUrl, price, quantityInStock, isAvailable)
        item.itemId = self.generateId()
        Items.append(item)

        return item
    

class EditProductItemForm(forms.Form):
    id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    name = forms.CharField(
        label='Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the name of the item',
            'class': 'w-full h-[40px] text-xl font-medium px-2 outline-none border-2 rounded-lg',  # Add any additional classes here
        }),
    )
    price = forms.FloatField(
        label='Price',
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'onkeydown': "return event.keyCode !== 69",
            'class': 'max-w-[120px] h-[40px] text-xl font-medium px-2 outline-none',
        }),
    )
    quantityInStock = forms.IntegerField(
        label='Quantity',
        required=True,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'onkeydown': "return event.keyCode !== 69",\
            'class': 'max-w-[120px] h-[40px] text-xl font-medium px-2 outline-none border-2 rounded-lg',
        }),
    )
    isAvailable = forms.BooleanField(
        label='Is Available',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-[25px] h-[25px] ml-3',
        }),
    )
    Image = forms.ImageField(
        label='Image',
        required=False,
    )


    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('price') <= 0: 
            self.add_error('price', 'Price cannot be 0 or negative')

        if cleaned_data.get('quantityInStock') < 0:
            self.add_error('quantityInStock', 'Quantity cannot be negative')

        if cleaned_data.get('isAvailable') == True and cleaned_data.get('quantityInStock') <= 0:
            self.add_error('isAvailable', 'Item cannot be available if there is no stock')

        return cleaned_data
    
    def save(self):
        cleaned_data = self.clean()

        id = cleaned_data.get('id')
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        quantityInStock = cleaned_data.get('quantityInStock')
        isAvailable = cleaned_data.get('isAvailable')
        ImageFile = cleaned_data.get('Image')

        #saving the image
        uploadedFileUrl = None
        if ImageFile != None and not isinstance(ImageFile, str):
            fs = FileSystemStorage()
            
            media_path = default_storage.save('uploads/' + ImageFile.name, ContentFile(ImageFile.read()))
            filename = fs.save(media_path, ImageFile)
            uploadedFileUrl = fs.url(filename)


        for item in Items:
            if item.itemId == id:
                item.name = name
                item.price = price
                item.quantityInStock = quantityInStock
                item.isAvailable = isAvailable
                item.totalPrice = item.calculate_total()
                if uploadedFileUrl != None:
                    item.Image = uploadedFileUrl
                break