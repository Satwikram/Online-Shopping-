from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from online.models import UserRegisteration
from main.views import products1
from django.core.mail import send_mail
from shopping.settings import EMAIL_HOST_USER
from random import randint
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from random import randint
from .models import *



def home(request):
    return render(request, 'home.html')

def register(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['psw']
        ph = request.POST['ph']
        password1 = request.POST['psw-repeat']

        if password1 != password:
            messages.info(request, "Password Mismatch!")
            return redirect("register")

        if UserRegisteration.objects.filter(phone = ph).exists():

            messages.info(request, "User Already Exist, Please Login ")
            return redirect('register')

        elif UserRegisteration.objects.filter(email = email).exists():

            messages.info(request, "Mail Id Exist, Please login with the same ")
            return redirect('register')

        else:

            otp = rnum()
            print(otp)

            email_otp = Otp()
            email_otp.otp = otp
            email_otp.email = email
            email.otp.save()

            online_user = UserRegisteration.objects.create(first_name = fname, last_name = lname,
                                               email = email, phone = ph)

            online_user.set_password(password)


            online_user.save()
            #messages.info(request, "User Created")
            print("User Created")
            subject = 'Registeration Successfull!'
            message = "hello Welcome to Lazy Shopping!\n " \
                      "Hope your doing great.\n" \
                      " Products you can sell:\n" \
                      "1.Mobiles\n" \
                      "2.Laptops\n" \
                      "for any query you can contact lazy@support.ac.in\n" \
                      "Have a great day!"


            recepient = email
            print("Email is:",recepient)
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

            subject1 = "OTP Verification!"
            to = [email]
            from_email = EMAIL_HOST_USER

            ctx = {
                'user': fname,
                'otp': otp
            }

            message1 = render_to_string('otp.html', ctx)

            msg = EmailMessage(subject1, message1, to=to, from_email=from_email)

            msg.content_subtype = 'html'
            msg.send()

            return redirect('otp')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        ph = request.POST['ph']
        password = request.POST['psw']
        user = UserRegisteration.objects.filter(phone = ph).first()
        user = authenticate(request, phone = ph, password = password)

        if user is not None:
            prods = products1()
            auth.login(request, user)

            return HttpResponseRedirect((reverse('main')))
        else:
            messages.info(request, "Invalid Phone Number or Password")

            return HttpResponseRedirect(reverse('login'))



    else:
        return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')



def contact(request):
    return render(request, 'contact.html')


def Logout(request):
    logout(request)
    prods = products1()

    return HttpResponseRedirect((reverse('main')))

def forgot(request):
    if request.method == 'POST':
        pass

    else:
        return render(request, 'forgot.html')

def rnum():
    return randint(1000,9999)

def otp(request):

    if request.method == 'POST':

        email = request.POST['email']
        otp = request.POST['otp']

        otp1 = Otp.objects.filter(email = 'email').values('otp')
        print(otp1)

        if otp != otp1:
            messages.info(request, "Invalid Otp for the Email")

        else:
            UserRegisteration.objects.filter(email = 'email').update(verified = True)
            Otp.objects.filter(email = 'email').delete()

            return redirect("main")

    else:
        return render(request, 'otp-verification.html')







