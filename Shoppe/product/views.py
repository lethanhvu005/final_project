import re

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django import views
from django.http import JsonResponse
from django.urls import reverse
from .models import Product
from .forms import Product
def myProduct(request):
    products = Product.objects.all()
    return render(request,'my_product.html',{'products':products})
def addProduct(request):
    image_err =[]
    if request.method == "POST":
        add_form = Product(request.POST)
        images = request.FILES.getlist('images')
        if not images:
            image_err.append('Cần chọn tối thiểu 1 ảnh')
        if len(images) > 3:
            image_err.append('Chọn tối đa ba ảnh') 
        type_image =['image/jpeg', 'image/png','image/jpg']
        for image in images:
            if image.content_type not in type_image:
                image_err.append('Chỉ nhận file jpeg ,png ,jpg')
            if image.size >= 1024 *1024:
                image_err.append(f"{image.name}cần nhỏ hơn 1 MB")           
        if add_form.is_valid() and not image_err:
            image_paths =[]
            for image in images:
                path =default_storage.save('product/'+image.name,image)
                image_paths.append(path)
            product = add_form.save(commit=False)
            product.image = image_paths[0]
            product.save()
            return JsonResponse({'success':'Tạo thành công',"redirect_url": reverse("product:my_product")})   
    else:
        add_form=Product()
    return render(request,'add_product.html',{'add_form':add_form,'image_err':image_err,})
def editProduct(request):
    user = request.user
    if request.method == 'POST':
        product = Product(request.POST,instance=user)
        return render(request,'edit_product.html', 'product':product)