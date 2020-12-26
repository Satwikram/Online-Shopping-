from rest_framework import serializers
from . import models
from .models import *

class SellSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellProduct

        fields = [
            'price',
            'product_name',
            'product_image',
            'product_des',
            'product_category',
            'date',
            'time',
        ]