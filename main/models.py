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


class AddCart(models.Model):
    user = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 150)
    quantity = models.IntegerField(default = 1)
    price = models.FloatField(max_length = 100)
    updated_price = models.FloatField(max_length = 100)
    product_name = models.CharField(max_length = 50)
    product_image = models.CharField(max_length = 100, null = True)
    product_des = models.TextField(max_length = 1000, blank = True)
    product_category = models.CharField(max_length = 50, blank = True)
    date = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)

class BillingDetailsS(models.Model):

    fname = models.CharField(max_length = 150)
    lname = models.CharField(max_length = 150)
    address = models.CharField(max_length = 1000)
    landmark = models.CharField(max_length = 1000, blank = True, null = True)
    state = models.CharField(max_length = 1000)
    postal = models.CharField(max_length = 1000)
    email = models.EmailField(verbose_name='email address',max_length=100, unique = True)
    phone = models.CharField(max_length = 150)
    notes = models.CharField(max_length = 1000)

class Orders(models.Model):

    user = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 150)
    product = models.ForeignKey(SellProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField(max_length = 100)
    updated_price = models.FloatField(max_length = 100)
    product_name = models.CharField(max_length = 50)
    product_image = models.CharField(max_length = 100, null = True)
    product_des = models.TextField(max_length = 1000, blank = True)
    product_category = models.CharField(max_length = 50, blank = True)
    datetime = models.DateTimeField(auto_now_add = True)
    delivery = models.CharField(max_length = 100, default = False)
