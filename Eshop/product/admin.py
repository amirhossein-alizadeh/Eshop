from django.contrib import admin
from .models import Product, ProductBrand, ProductCategory, ProductTag
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'price',
        'is_active'
    ]
    list_editable = [
        'is_active'
    ]
    list_filter = [
        'is_active'
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(ProductBrand)