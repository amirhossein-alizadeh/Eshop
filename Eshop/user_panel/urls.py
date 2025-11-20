from django.urls import path

from .views import EditProfileView, UserPanelView

urlpatterns = [
    path("", UserPanelView.as_view(), name="user_panel"),
    path("edit-profile", EditProfileView.as_view(), name="edit_profile")
]