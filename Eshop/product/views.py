from django.shortcuts import render
from .models import Product

def product_list(request):
    product_list = Product.objects.all()
    return render(
        request,
        "product/product_list.html",
        {
            "products":product_list
        }
    )