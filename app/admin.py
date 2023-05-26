from django.contrib import admin
from .models import Product, Brand, Category, Warranty

# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Warranty)