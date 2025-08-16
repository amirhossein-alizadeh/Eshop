from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'نام و نام خانوادگی',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'ایمیل',
                'class': 'form-control'
            }
        )
    )
    subject = forms.CharField(
        label='موضوع',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'موضوع',
                'class': 'form-control'
            }
        )
    )
    message = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'متن پیام',
                'class': 'form-control',
                'id': 'message'
            }
        )
    )