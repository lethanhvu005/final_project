from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse 
from django.template.loader import render_to_string
from product.models import Product
def index(request):
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
    return render(request,'index.html',{'products':products,'search_url':reverse('shop:search')})
def search_prd(search_content):
    products = Product.objects.order_by('-id')
    if search_content:
        products = Product.objects.filter(name__icontains=search_content).order_by('-id')
    return products
def search(request):
    search_content = request.GET.get('q','').strip()
    products =search_prd(search_content)
    return render(request, "index.html", {
        "products": products,
        "search_url": reverse("shop:search"),
    })
def search_advanced(request):
    products = Product.objects.all()
    if request.method == 'POST':
        price = request.POST.get('price')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        status = request.POST.get('status')
        name =request.POST.get('name')
        if name:
            products = products.filter(name__icontains=name)
        if category:
            products = products.filter(category__name__icontains=category)
        if brand:
            products = products.filter(brand__name__icontains=brand)
        if status:
            products = products.filter(status=status)
        if price == '1':
            products = products.filter(price__range=(0,50))
        elif price == '2':
            products = products.filter(price__range=(51,100))
        elif price == '3':
            products = products.filter(price__range=(101,200))
        elif price == '4' :
            products = products.filter(price__gt=201)
        html= render_to_string('product_list.html',{
            'products':products
        },request=request)
        return JsonResponse({'success':"done",'html':html})
    return render(request,'index.html',{'products':products})
def search_price(request):
    products = Product.objects.all()
    if request.method =="POST":
        min = request.POST.get('min')
        max = request.POST.get('max')
        products = products.filter(price__range=(min,max))
        html = render_to_string('product_list.html',{'products':products},request=request)
        return JsonResponse({'success':'done','html':html})
    return render(request,'index.html',{'products':products,'search_url':'shop:search_price'})