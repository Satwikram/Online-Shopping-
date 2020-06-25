import os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from main.models import products, selling


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
        print(des)

        try:
            folder = 'media/images/'
            uploaded_image = request.FILES['prod']
            print("Name is:", uploaded_image.name)

            # if not uploaded_image:
            # return Response({"error": "Choose file"}, status=status.HTTP_400_BAD_REQUEST)
            # for f in myfiles:
            filename = str(uploaded_image.name)
            fs = FileSystemStorage(location=folder)  # defaults to DATASTORE
            name = fs.save(uploaded_image.name, uploaded_image)
            mediapath = folder + 'user.name' + "{}"
            filepath = os.path.join(mediapath).format(name)
            print(filepath)

            product = selling()
            product.price = price
            product.product_name = pname
            product.product_image = filepath
            product.product_des = des
            product.save()

        except Exception as e:
            print("Error is:",e)

        return HttpResponseRedirect((reverse('main')))


    else:
        return render(request, 'sell.html')

def buy(request):
    return render(request, 'description.html')