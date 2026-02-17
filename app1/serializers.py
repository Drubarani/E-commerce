from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSeializer):
    class Meta:
        model = Product 
        fields='__all__'

class OrderSerializer(serializers.ModelSeializer):
    class Meta:
        model = Order
        fields='__all__'

