from django.urls import path
from .views import product_detail, product_list

urlpatterns = [
    path("", product_list, name="products"),
    path('<slug:product_slug>', product_detail, name="product_detail")
]
