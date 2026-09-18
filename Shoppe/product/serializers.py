from dataclasses import field
from unittest import mock
from rest_framework import serializers
from .models import Product
class ProductSerializers(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields ="__all__"