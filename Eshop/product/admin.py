from django.contrib import admin
from .models import Product, ProductCategory
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':['title']
    }
    list_display = [
        '__str__',
        'price',
        'rating',
        'is_active'
    ]
    list_editable = [
        'is_active'
    ]
    list_filter = [
        'rating',
        'is_active'
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)