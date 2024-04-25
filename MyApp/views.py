from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from accounts.models import *
from django.contrib import messages
# Create your views here.


def home(request):
    return HttpResponse(f"<h1> Mother Khanki </h1><br><h2>{request}</h2>")


def page(request):
    return render(request,"test1.html")


def product(request):
    products = []
    for product in Product.objects.all():
        products.append({'id':product.id,'name':product.name,'price':product.price,'rating':product.rating})
    return render(request,"productTable.html",context={'products':products})


def addProduct(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        try:
            price = float(data.get("price"))
            rating = int(data.get("rating"))
            if rating > 5:
                messages.warning(request,"Rating must be between 1 and 5")
                return redirect("/add-product/")
            Product.objects.create(name=name,price=price,rating=rating)

            messages.success(request,"Product added successfully")
            return redirect('/add-product/')
        except:
            messages.error(request,"Something went wrong. Please enter data properly")
            return redirect('/add-product/')
    return render(request,'productForm.html')


def deleteProduct(request,id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/products/')


def updateProduct(request,id):
    if request.method == 'POST':
        obj = Product.objects.filter(id=id)[0]
        try:
            data = request.POST
            name = data.get('name')
            if name=='':
                name = obj.name
            if data.get('price') != '':
                price = float(data.get('price'))
            else:
                price = obj.price
            if data.get('rating') != '':
                rating = int(data.get('rating'))
            else:
                rating = obj.rating
            obj.name = name
            obj.price = price
            obj.rating = rating
            obj.save()
        except:
            messages.error(request,"Something went wrong. Please enter data properly")
            return redirect("/update/")
        return redirect(f"/update/")
    return render(request,'updateProduct.html')
