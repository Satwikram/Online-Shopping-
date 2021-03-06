from rest_framework import serializers
from . import models
from .models import *

class SellSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellProduct

        fields = [
            'id',
            'slug',
            'price',
            'product_name',
            'product_image',
            'product_des',
            'product_category',
            'date',
            'time',
        ]

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddCart

        fields = [
            'id',
            'user',
            'slug',
            'quantity',
            'price',
            'updated_price',
            'product_name',
            'product_image',
            'product_des',
            'product_category',
            'date',
            'time',
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerOrders
        fields = '__all__'