from django.contrib import admin
from .models import Category, Service, Reviews, Order
# Register your models here.


admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Reviews)
admin.site.register(Order)
