from django import forms
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

class RegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(),
        label="ایمیل",
        validators=[
            EmailValidator(),
            MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        max_length=120,
        label="رمز عبور",
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(16)
        ]
    )
    confirm_password = forms.CharField(
        max_length=120,
        label="تکرار رمز عبور",
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(16)
        ]
    )
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("رمز عبور و تکرار رمز عبور مغایرت دارند")
        
        
class LoginForm(forms.Form):
    email = forms.CharField(
        label="ایمیل",
        widget=forms.EmailInput(),
        max_length=100,
        validators=[
            EmailValidator(),
            MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        label="رمز عبور",
        max_length=16,
        widget=forms.TextInput(),
        validators=[
            #MinLengthValidator(8),
            MaxLengthValidator(16)
        ]
    )
    
    
class ForgotPasswordForm(forms.Form):
    email = forms.CharField(
        label="ایمیل",
        widget=forms.EmailInput(),
        max_length=100,
        validators=[
            EmailValidator(),
            MaxLengthValidator(100)
        ]
    )
    
    
class ResetPasswordForm(forms.Form):
    
    password = forms.CharField(
        max_length=120,
        label="رمز عبور",
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(16)
        ]
    )
    confirm_password = forms.CharField(
        max_length=120,
        label="تکرار رمز عبور",
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(16)
        ]
    )
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("رمز عبور و تکرار رمز عبور مغایرت دارند")
