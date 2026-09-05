from django.shortcuts import render
from product.models import Product
def home(request):
    products = Product.objects.order_by('-id')[:6]
    return render(request,'home.html',{'products':products,})
