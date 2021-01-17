import os
from datetime import datetime
from datetime import date
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
import requests
from .serializers import *
from main.models import products, SellProduct, CustProduct

"""
Author: Satwik Ram K
Rest API
"""

class ProductsAPIView(generics.ListCreateAPIView):

    queryset = SellProduct.objects.all()
    serializer_class = SellSerializer

class ProductDetailsAPIView(APIView):

    def get_object(self, slug):
        try:
            id = SellProduct.objects.all().filter(slug = slug).values('id')[0]['id']
            product = SellProduct.objects.filter(id = id).values()
            return product

        except SellProduct.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)


    def get(self, request, slug):

        try:
            product = self.get_object(slug)
            serializer = SellSerializer(product, many = True)

            return Response(serializer.data, status=status.HTTP_200_OK)
            #return render(request, "results.html", {'results': details})

        except Exception as e:
            print("Error is",e)
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)


class SearchListAPIView(ListAPIView):

    queryset = SellProduct.objects.all()
    serializer_class = SellSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('product_name', 'product_des', 'product_category')

class CartAPIView(APIView):

    def get_object(self, user):
        try:
            details = AddCart.objects.all().filter(user = user).values()
            return details
        except AddCart.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, user):

        details = self.get_object(user)
        serializer = CartSerializer(details,  many = True)
        return Response(serializer.data)

    def post(self, request, user):

        serializer = CartSerializer(data = request.data)

        if serializer.is_valid():
            slug = serializer.validated_data['slug']
            price = serializer.validated_data['price']
            print(slug, price)

            if AddCart.objects.filter(user = user).exists():
                if AddCart.objects.filter(slug = slug).exists():
                    quantity = AddCart.objects.filter(user = user, slug = slug).values('quantity')[0]['quantity']
                    print(quantity)
                    quantity = quantity + 1
                    updated_price = quantity * price
                    AddCart.objects.filter(user = user, slug = slug).update(quantity = quantity, updated_price = updated_price)
                    print("Updated Successfully")
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    serializer.save()
                    print("Added Successfully")
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.save()
                print("Added Successfully")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pass
"""
Author: Satwik Ram K
Django API
"""
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
            filepath = filepath+name
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

def details(request):
    pass


def search(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        query = "?search="+query
        url = "http://127.0.0.1:8000/search/"+query
        response = requests.get(url)
        results = response.json()
        if results == []:
            messages.info(request,"No Results Found")
            return render(request, 'notfound.html')
        return render(request, "results.html", {'results': results})


def buy(request, slug):
   slug = slug
   url = "http://127.0.0.1:8000/details/"+slug

   response = requests.get(url)
   results = response.json()
   print("Results",results)
   if results == []:
    messages.info(request,"This item is out of Stock")
    return render(request, 'notfound.html')
   return render(request, "description.html", {'results': results})


def addcart(request, slug):

    slug = slug
    url = "http://127.0.0.1:8000/details/"+slug
    response = requests.get(url)
    result = response.json()
    result = result[0]
    user = request.user
    user = str(user)
    result['user'] = user
    result['quantity'] = 1
    result['updated_price'] = result['price'] * result['quantity']

    print(result['updated_price'])

    print(result)


    if result == []:
        messages.info(request, "This item is out of Stock")
        return HttpResponseRedirect((reverse('main')))

    url1 = "http://127.0.0.1:8000/add-to-cart/"+user
    requests.post(url1, data = result)

    messages.info(request, "Sucessfully Added to Cart")
    return HttpResponseRedirect((reverse('main')))

def cart(request, user):

    if user == 'AnonymousUser':
        return HttpResponse("Please Login to View the Cart.")
    else:
        url = 'http://127.0.0.1:8000/add-to-cart/'+user
        response = requests.get(url = url)
        results = response.json()
        print("obtained Result is",results)
        total = 0
        for result in results:
            total += result['updated_price']

        if total <1000:
            shipping = 100
            total = total + shipping
        else:
            shipping = 0
        return render(request, "cart.html", {"results": results, "total": total, "shipping": shipping})

def checkout(request):
    return render(request, "checkout.html")