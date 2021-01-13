from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

from shopping.utils import unique_slug_generator


class products:

    name : str
    img : str
    price : int
    des : str

class CustProduct:

    name : str
    img : str
    price : float
    des : str
    cat : str

'''
Created by : Satwik Ram K
version : 1
'''
class SellProduct(models.Model):

    slug = models.SlugField(unique = True, max_length=250, null=True, blank=True, editable = False)
    price = models.FloatField(max_length = 10)
    product_name = models.CharField(max_length = 50)
    product_image = models.CharField(max_length = 100, null = True)
    product_des = models.TextField(max_length = 1000, blank = True)
    product_category = models.CharField(max_length = 50, blank = True)
    date = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)

    def __str__(self):
        return self.product_name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender = SellProduct)


class Cart(models.Model):
    product = models.ForeignKey(SellProduct, related_name = "Add_to_Cart",on_delete=models.CASCADE)
    price = models.FloatField(max_length = 10)
    product_name = models.CharField(max_length = 50)
    product_image = models.CharField(max_length = 100, null = True)
    product_des = models.TextField(max_length = 1000, blank = True)
    product_category = models.CharField(max_length = 50, blank = True)
    date = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)
