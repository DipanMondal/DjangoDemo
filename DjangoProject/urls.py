"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import MyApp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',accounts.views.home,name='home'),
    path('admin-login/',accounts.views.adminLogin,name='adminLogin'),
    path('client-login/',accounts.views.clientLogin,name='clientLogin'),
    path('admin-signup-form/',accounts.views.adminSignUp,name='admin_signup'),
    path('client-signup-form/',accounts.views.clientSignUp,name='client_signup'),
    path('chat/',MyApp.views.page,name='chat'),
    path('products/',MyApp.views.product,name='products'),
    path('add-product/',MyApp.views.addProduct,name='add_product'),
    path('delete/<id>/',MyApp.views.deleteProduct,name='deleteProduct')
]
