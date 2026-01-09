from django import forms
from django.core.exceptions import ValidationError

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


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="رمز عبور فعلی"
    )
    new_password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="رمز عبور جدید"
    )

    confirm_new_password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="تکرار رمز عبور جدید"
    )

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm = self.cleaned_data.get("confirm_new_password")

        if new_password == confirm:
            return confirm
        raise ValidationError("رمز عبور جدید و تکرار رمز عبور جدید با هم مغایرت دارند")