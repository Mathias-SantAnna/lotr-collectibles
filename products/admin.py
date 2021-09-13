from django.contrib import admin
from .models import Category, Brand, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'brand',
        'name',
        'has_sizes',
        'price',
        'is_discount',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin) 