from django.db.models.aggregates import Count
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from site_settings.models import CommercialBanner
from utils.http_service import get_ip
from .models import Product, ProductCategory, ProductBrand, ProductVisit


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        banners = CommercialBanner.objects.filter(is_active=True,
                                                  position=CommercialBanner.BannerPosition.products_list_page).all()
        data["banners"] = banners
        print(data)
        return data


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        product = self.object
        user_ip = get_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        visited_by_user = ProductVisit.objects.filter(product_id=product.id, ip=user_ip).exists()
        if not visited_by_user:
            new_visit = ProductVisit(product=product, ip=user_ip, user_id=user_id)
            new_visit.save()

        return data



def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False).all()
    context = {
        "categories": product_categories
    }
    return render(request, "product/components/product_categories_component.html", context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.filter(is_active=True).annotate(products_count=Count("products")).all()

    context = {
        "brands": product_brands
    }
    return render(request, "product/components/product_brands_component.html", context)
