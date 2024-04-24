from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.


def home(request):

    return render(request,'home.html')


def adminSignUp(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        conf_password = data.get('conf_password')
        if password != conf_password or len(phone) < 10:
            return redirect('/admin-signup-form/')
        Admin.objects.create(name=name,phone=phone,email=email,password=password)
        return redirect('/admin-login/')
    return render(request,'adminSignUp.html')


def clientSignUp(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        conf_password = data.get('conf_password')
        if password != conf_password or len(phone) < 10:
            return redirect('/client-signup-form/')
        Client.objects.create(name=name,phone=phone,email=email,password=password)
        return redirect('/client-login/')
    return render(request,'clientSignUp.html')


def clientLogin(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        try:
            obj = Client.objects.get(email=email)
            if obj.get('password') == password:
                return redirect('/chat/')
        except:
            return redirect('/client-login/')
    return render(request, 'clientLogin.html')


def adminLogin(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        try:
            obj = Admin.objects.filter(email=email)[0]
            if obj.password == password:
                return redirect('/products/')
        except:
            return redirect('/admin-login/')
    return render(request,'adminLogin.html')