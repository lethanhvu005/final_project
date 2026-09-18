from django.urls import path
from . import views
app_name ='product'
urlpatterns = [
        path('my_product/',views.myProduct,name='my_product'),
        path('add_product/',views.addProduct,name='add_product'),
        path('edit_product/<int:id>',views.editProduct,name='edit_product'),
        path('delete_product/<int:id>',views.deleteProduct,name='delete_product'),
        path('product_detail/<int:id>',views.productDetail,name='product_detail'),
        path('api/list/', views.prd_api_list, name='product_list_api'),
        path('api/add/', views.prd_add, name='prd_add'),
        path('api/edit/<int:id>', views.edit_prd, name='edit_prd'),


        ]
    