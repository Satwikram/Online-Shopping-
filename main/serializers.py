from rest_framework import serializers
from . import models
from .models import *

class SellSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellProduct

        fields = [
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
            'user',
            'slug',
            'quantity',
            'price',
            'product_name',
            'product_image',
            'product_des',
            'product_category',
            'date',
            'time',
        ]