from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(),
        label="ایمیل"
    )
    password = forms.CharField(
        max_length=120,
        label="رمز عبور",
    )
    confirm_password = forms.CharField(
        max_length=120,
        label="تکرار رمز عبور",
    )