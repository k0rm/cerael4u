from django.forms import ModelForm, widgets
from django import forms
from products.models import Product

class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'brand': widgets.Select(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
        }

class ProductCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Product
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'brand': widgets.Select(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
        }