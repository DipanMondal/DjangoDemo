from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages

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
            messages.info(request,"")
            return redirect('/admin-signup-form/')
        Seller.objects.create(name=name,phone=phone,email=email,password=password)
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
        user = Consumer.objects.filter(email=email)
        if user.exists():
            messages.info(request, f"User ID:{email} already exists")
            return redirect('/client-signup-form/')
        if password != conf_password or len(phone) < 10:
            messages.info(request,"Enter password and confirm password correctly")
            return redirect('/client-signup-form/')
        Consumer.objects.create(name=name,phone=phone,email=email,password=password)
        messages.success(request, "Account created successfully")
        return redirect('/client-login/')
    return render(request,'clientSignUp.html')


def clientLogin(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        obj = Seller.objects.filter(email=email)
        if not obj.exists():
            messages.error(request, "User doesn't exists")
            return redirect('/client-login/')
        elif obj[0].password == password:
            return redirect(f'/chat/{obj[0].id}/')
        else:
            messages.error(request, "Invalid Password")
            return redirect('/client-login/')
    return render(request, 'clientLogin.html')


def adminLogin(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        obj = Seller.objects.filter(email=email)
        if not obj.exists():
            messages.error(request,"User doesn't exists")
            return redirect('/admin-login/')
        elif obj[0].password == password:
            return redirect(f'/products/')
        else:
            messages.error(request, "Invalid Password")
            return redirect('/admin-login/')
    return render(request,'adminLogin.html')