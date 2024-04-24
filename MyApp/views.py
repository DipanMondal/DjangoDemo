from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from accounts.models import *
# Create your views here.


def home(request):
    return HttpResponse(f"<h1> Mother Khanki </h1><br><h2>{request}</h2>")


def page(request):
    return render(request,"test1.html")


def product(request,admin_id):
    queue = Admin.objects.filter(id=admin_id)
    if len(queue) == 0:
        return HttpResponse("<h1>Error !</h1><br><a href='/admin-login/'>return to login page</a>")
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
                return HttpResponse("<h1>Chal Fot</h1><h2>rating 5 er niche de bara</h2>")
            Product.objects.create(name=name,price=price,rating=rating)
            return HttpResponse("<h1>Thanks for submission</h1><br><a href='/products/'>return to product menu  </a>")
        except:
            return HttpResponse("<h1>Something Went Wrong</h1><h2>Thik thak data de bolod</h2>")
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
            return HttpResponse(f"""<h2>There was something wrong with input data</h2><br>
                                <a href='/update/{id}/'>Return to update</a><br>
                                <a href='/products/'>Return to Product menu</a>""")
        return redirect(f"/products/")
    return render(request,'updateProduct.html')
