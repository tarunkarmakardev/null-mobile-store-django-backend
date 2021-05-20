from django.contrib import admin
from .models import Product, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'price', ]
    list_display_links = ['id', 'name', 'brand', 'price', ]
    list_filter = ['brand']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['id', 'name', ]
