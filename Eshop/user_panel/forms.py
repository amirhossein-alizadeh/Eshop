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
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
            "about_user": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control",
                }
            )
        }