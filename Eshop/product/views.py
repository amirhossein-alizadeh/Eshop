from django.shortcuts import get_object_or_404, render
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
    
    
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    return render(
        request, 
        "product/product_detail.html",
        {
            "product": product
        }
    )