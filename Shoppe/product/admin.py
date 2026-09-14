from django.contrib import admin
from .models import Product,Brand,Category
@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display=(
        'name',)
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display=(
        'name',)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'category',
        'brand',
        'status',
    )

    search_fields = ('name',)