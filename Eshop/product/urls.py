from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("cat/<str:cat>", ProductListView.as_view(), name="products_category_filter"),
    path("brand/<str:brand>", ProductListView.as_view(), name="products_brand_filter"),
    path('<slug:slug>', ProductDetailView.as_view(), name="product_detail")
]
