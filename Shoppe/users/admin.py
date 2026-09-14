from django.contrib import admin
from .models import UserCustomer
@admin.register(UserCustomer)
class Admin(admin.ModelAdmin):
    list_display =(
        'password',
        'is_superuser',
        'username',
        'email',
    )
    