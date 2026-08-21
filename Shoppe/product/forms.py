from dataclasses import field
from django import forms
from .models import Product
class Product(forms.ModelForm):
    class Meta():
        model = Product
        fields =['name','price','category','brand','status','sale','company','detail']
