from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('',views.main_cart,name='cart_main'),
    path('checkout/',views.checkout,name='checkout'),
    path('prdUp/',views.Quantity,name='prdUp')
]
