from django import forms
from account.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "avatar",
            "about_user",
            "address"
        ]