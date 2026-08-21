from django.urls import path
from . import views
app_name ='product'
urlpatterns = [
        path('my_product/',views.myProduct,name='my_product'),
        path('add_product/',views.addProduct,name='add_product')
    ]
    