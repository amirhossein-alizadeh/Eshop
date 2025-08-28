from django.urls import path

from .views import ActivateAccount, ForgotPasswordView, LoginView, RegisterView, ResetPasswordView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("activate-account/<str:activate_code>", ActivateAccount.as_view(), name="activate_account"),
    path("forget-password/", ForgotPasswordView.as_view(), name="forget_pass"),
    path("reset-password/<str:email_active_code>", ResetPasswordView.as_view(), name="reset_password")
]
