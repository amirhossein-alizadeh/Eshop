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
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("رمز عبور و تکرار رمز عبور مغایرت دارند")