from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get("cat")
        brand_name = self.kwargs.get("brand")
        if category_name:
            query = query.filter(category__title_in_url__iexact=category_name)
        if brand_name:
            query = query.filter(brand__title_in_url__iexact=brand_name)

        return query

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False).all()
    context = {
        "categories": product_categories
    }
    return render(request, "product/components/product_categories_component.html", context)

def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.filter(is_active=True).all()
    context = {
        "brands": product_brands
    }
    return render(request, "product/components/product_brands_component.html", context)

