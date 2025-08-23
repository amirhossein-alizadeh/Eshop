from os import name
from django.urls import path

from .views import ActivateAccount, LoginView, RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("activate-account/<str:activate_code>", ActivateAccount.as_view(), name="activate_account")
]
