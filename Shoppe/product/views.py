import re
from django.shortcuts import render, redirect,get_object_or_404
from django.core.files.storage import default_storage
from django import views
from django.http import JsonResponse
from django.urls import reverse
from .models import Product,Brand
from .forms import ProductForm
def myProduct(request):
    products = Product.objects.all()
    return render(request,'my_product.html',{'products':products})
def addProduct(request):
    image_err =[]
    if request.method == "POST":
        add_form = ProductForm(request.POST)
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
            product.image = image_paths
            product.save()
            return JsonResponse({'success':'Tạo thành công',"redirect_url": reverse("product:my_product")})   
    else:
        add_form=ProductForm()
    return render(request,'add_product.html',{'add_form':add_form,'image_err':image_err,})
def editProduct(request,id):
    product = get_object_or_404(Product,id=id)
    image_err =[]
    if request.method == 'POST':
        product_edit = ProductForm(request.POST,instance=product,)
        images = request.FILES.getlist('images')
        if len(images) > 3:
            image_err.append('Chọn tối đa ba ảnh') 
        type_image =['image/jpeg', 'image/png','image/jpg']
        for image in images:
            if image.content_type not in type_image:
                image_err.append('Chỉ nhận file jpeg ,png ,jpg')
            if image.size >= 1024 *1024:
                image_err.append(f"{image.name}cần nhỏ hơn 1 MB") 
        if product_edit.is_valid() and not image_err:
            image_paths =[]
            image_delete = request.POST.getlist('image_delete')
            image_old = product.image or []
            if isinstance(image_old, str):
                image_old = [image_old]
            else:
                image_old = list(image_old)
            image_delete=[
                path
                for path in image_delete
                if path in image_old
            ]
            remaining_images =[
                path 
                for path in image_old
                if path not in image_delete
            ]
            total_images = len(remaining_images)+len(images)
            product = product_edit.save(commit=False)
            if total_images >3:
                return JsonResponse({'err':'Chỉ nhận tối đa ba ảnh',})   
            else:
                for image in images:
                    path =default_storage.save('product/'+image.name,image)
                    image_paths.append(path)
                image_new = remaining_images + image_paths
                product.image = image_new
                product.save( )
                for path in image_delete:
                    if default_storage.exists(path):
                        default_storage.delete(path)
                return JsonResponse({
                "success": True,
                "redirect_url": reverse("product:my_product"),})
    else:
        product_edit=ProductForm(instance=product)
    return render(request,'edit_product.html', {'product_edit':product_edit,'image_err':image_err,'product':product})
def deleteProduct(id):
    product= get_object_or_404(Product,id=id)
    product.delete()
    return redirect('product:my_product')
def productDetail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'product_detail.html',{'product':product,})