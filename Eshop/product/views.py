from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product



class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(price__gt=200000)
    #     return data
    
class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    