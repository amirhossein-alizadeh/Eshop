from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home.as_view(), name="home"),
    path("product_list/", include("product.urls"))
]
