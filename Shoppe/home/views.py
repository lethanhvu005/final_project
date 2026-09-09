from math import e

from django.shortcuts import render
from product.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
app_name ='home'
def home(request):
    search_content = request.GET.get('q','').strip()
    if search_content:
        products = Product.objects.filter( name__icontains=search_content).order_by('-id')
    else:
        products = Product.objects.order_by('-id')[:6]
    if request.method=='POST':
        id = request.POST.get('id')
        product = Product.objects.get(id=id)
        prd_id =str(product.id)
        cart = request.session.get('cart',{})
        if prd_id in cart:
            cart[prd_id]['quantity'] +=1
        else:
            cart[prd_id]={'quantity':1}
        request.session['cart']= cart
        count = len(cart)
        request.session['count_cart']=count
        return JsonResponse({'success':'Tạo thành công','count':count})  
    return render(request,'home.html',{'products':products,})
