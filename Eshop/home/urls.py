from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home.as_view(), name="home"),
    path("products/", include("product.urls"))
]
