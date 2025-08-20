from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product



class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 1
    
class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    