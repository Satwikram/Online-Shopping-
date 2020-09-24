from django.db import models

# Create your models here.

class products:

    name : str
    img : str
    price : int
    des : str

'''
Created by : Satwik Ram K
version : 1
'''
class SellProducts(models.Model):
    price = models.FloatField(max_length = 10)
    product_name = models.CharField(max_length = 50)
    product_image = models.CharField(max_length = 100, null = True)
    product_des = models.TextField(max_length = 1000, blank = True)
    date = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)
