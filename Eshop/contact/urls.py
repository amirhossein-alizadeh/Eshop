from django.urls import path

from .views import ContactUsPage

urlpatterns = [
    path('', ContactUsPage.as_view(), name='contact')
]
