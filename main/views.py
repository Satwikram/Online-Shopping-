import os
from datetime import datetime
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from .serializers import *

from main.models import products, SellProduct, CustProduct


def products1():
    prod1 = products()
    prod1.price = 1000
    prod1.img = 'shoe_1.jpg'
    prod1.name = 'Corater'
    prod1.des = 'Finding perfect products'

    top = products()
    top.price = 700
    top.img = 'cloth_1.jpg'
    top.name = 'Tank Top'
    top.des = 'Finding perfect t-shirt'

    polo = products()
    polo.price = 600
    polo.img = 'cloth_2.jpg'
    polo.name = 'Polo Shirt'
    polo.des = 'Finding perfect Polo T-shirts'

    coarter = products()
    coarter.price = 600
    coarter.img = 'shoe_1.jpg'
    coarter.name = 'Coarter'
    coarter.des = 'Finding perfect Shoes'

    canon = products()
    canon.price = 36000
    canon.img = 'canon.jpg'
    canon.name = 'Canon Ultimate'
    canon.des = 'Camera with 4K recording and ultimate graphics'


    prods = [prod1, top, polo, coarter, canon, prod1, top, polo, coarter, canon,prod1, top, polo, coarter, canon,]

    return prods

def CustProducts():
    products = SellProduct.objects.all()
    return products

class SearchListAPIView(ListAPIView):

    queryset = SellProduct.objects.all()
    serializer_class = SellSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('product_name', 'product_des', 'product_category')


def Main(request):

    prods = products1()

    return render(request, "index.html", {'prods' : prods})

def collection(request):

    prods = products1()

    return render(request, 'try.html', {'prods': prods})


def sell(request):

    if request.method == 'POST':
        pname = request.POST['pname']
        price = request.POST['price']
        des = request.POST['des']
        cat = request.POST['cat']
        print(des)
        print(cat)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        today = date.today()
        print("Today's date:", today)

        try:
            folder = 'media/images/Products/'
            uploaded_image = request.FILES['prod']
            print("Name is:", uploaded_image.name)

            # if not uploaded_image:
            # return Response({"error": "Choose file"}, status=status.HTTP_400_BAD_REQUEST)
            # for f in myfiles:
            filename = str(uploaded_image.name)
            mediapath = folder + "{}/"
            user_ph = request.user.phone
            print("User Name:",user_ph)
            filepath = os.path.join(mediapath).format(user_ph)
            fs = FileSystemStorage(location=filepath)  # defaults to DATASTORE
            name = fs.save(uploaded_image.name, uploaded_image)
            print(filepath)

            product = SellProduct()
            product.price = price
            product.product_name = pname
            product.product_image = filepath
            product.product_des = des
            product.time = current_time
            product.date = today
            product.product_category = cat
            product.save()

        except Exception as e:
            print("Error is:",e)

        return HttpResponseRedirect((reverse('main')))

    else:
        return render(request, 'sell.html')

def buy(request):
    prods = products1()
    return render(request, 'description.html', {'prods': prods})
