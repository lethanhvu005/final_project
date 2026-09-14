from django.contrib import admin
from .models import History
@admin.register(History)
class AdminHistory(admin.ModelAdmin):
    list_display=('user',
            'email',
            'name',
            'phone',
            'price')
