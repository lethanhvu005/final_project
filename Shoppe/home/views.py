from math import e
from django.template.loader import render_to_string

from django.shortcuts import render
from django.urls import reverse

from shop.views import search_prd
from product.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
app_name ='home'
def home(request):
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
        return JsonResponse({'success':'Tạo thành công','count':count,})  
    return render(request,'home.html',{'products':products,"search_url": reverse("search")})
def search(request):
    search_content = request.GET.get('q','').strip()
    products = search_prd(search_content)
    return render(request,'home.html',{"products": products,"search_url": reverse("search")})
def search_price(request):
    products = Product.objects.all()
    if request.method =="POST":
        min = request.POST.get('min')
        max = request.POST.get('max')
        products = products.filter(price__range=(min,max))
        html = render_to_string('product_list.html',{'products':products},request=request)
        return JsonResponse({'success':'done','html':html})
    return render(request,'home.html',{'products':products,'search_url':'search_price'})