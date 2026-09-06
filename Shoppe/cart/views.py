import re

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.http import JsonResponse
@login_required
def Cart(request):
    cart = request.session.get('cart',{})
    products=[]
    cart_total=0
    for id,item in cart.items():
        product = Product.objects.get(id=int(id))
        total = item['quantity']*product.price
        cart_total += total
        products.append({
            'prd':product,
            'quantity':item['quantity'] ,
            'total':total,
        })
    return render(request,'cart.html',{'products':products,'cart_total':cart_total})
def Quantity(request):
    if request.method == 'POST':
        idPrd = request.POST.get('idPrd')
        upPrd = request.POST.get('upPrd')
        product = Product.objects.get(id=idPrd)
        downPrd = request.POST.get('downPrd')
        deletePrd =request.POST.get('deletePrd')
        id = str(idPrd)
        cart = request.session.get('cart',{})
        if id in cart:
            if(deletePrd =='1'):
                cart.pop(id)
                request.session['cart']= cart
                cart_total=0
                for prd_id, item in cart.items():
                    prd = Product.objects.get(id=prd_id)
                    cart_total += item['quantity'] * prd.price
                return JsonResponse({'success':'Xóa thành công','deleted':True,'cart_total':cart_total})
            if upPrd == '1' and downPrd == '0':
                cart[id]['quantity'] +=1
                total = cart[id]['quantity']* product.price
            elif(upPrd == '0' and downPrd == '1'):
                if cart[id]['quantity'] > 1:
                    cart[id]['quantity'] -=1                
                    total = cart[id]['quantity']* product.price
            request.session['cart']= cart
            cart_total=0
            for prd_id, item in cart.items():
                prd = Product.objects.get(id=prd_id)
                cart_total += item['quantity'] * prd.price
            quantity = cart[id]['quantity']
        return JsonResponse({'success':'Thành công','quantity':quantity,'total':total,'cart_total':cart_total})
    return JsonResponse({'error':'Lỗi'})
