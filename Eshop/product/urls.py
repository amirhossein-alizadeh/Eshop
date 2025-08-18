from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path('<slug:slug>', ProductDetailView.as_view(), name="product_detail")
]
