from django.contrib import admin
from accounts.models import *
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Seller)
admin.site.register(Consumer)
