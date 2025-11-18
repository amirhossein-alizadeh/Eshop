from django.urls import path

from .views import EditProfileView

urlpatterns = [
    path("", EditProfileView.as_view(), name="edit_profile_page")
]