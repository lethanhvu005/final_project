from django.contrib import admin
from .models import Country , UserCustomer
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display =('name',)
    search_fields=('name',)
@admin.register(UserCustomer)
class UserAdmin(admin.ModelAdmin):
    list_display = (
    'password',
    'is_superuser',
    'username',
    'first_name',
    'last_name',
    'email',
    'is_staff',
    'is_active',
    'avatar',
    'confirm_password',
    'id_country_id',
)
    search_fields=('username','email',)
    list_filter=('username','email',)