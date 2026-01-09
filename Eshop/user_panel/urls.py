from django.urls import path

from .views import EditProfileView, UserPanelView, ChangePasswordView

urlpatterns = [
    path("", UserPanelView.as_view(), name="user_panel"),
    path("edit-profile", EditProfileView.as_view(), name="edit_profile"),
    path("change-password", ChangePasswordView.as_view(), name="change_password")
]