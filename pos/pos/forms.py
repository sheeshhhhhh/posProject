from django import forms


class ProductItemForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,  required=True)
    price = forms.FloatField(label='Price',  required=True)
    quantityInStock = forms.IntegerField(label='Quantity', required=True)
    isAvailable = forms.BooleanField(label='Is Available', required=True)
    Image = forms.ImageField(label='Image', required=True)
    #category = forms.CharField(label='Category', max_length=100)

    def clean(self):
        self.cleaned_data = super().clean()

        #check in the array if the name already exists
        #check if the id already exist
        

