from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('search_advanced/',views.search_advanced,name='search_advanced'),
    path('search_price/',views.search_price, name='search_price'),
]
