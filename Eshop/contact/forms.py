from django import forms

from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields =[
            'subject',
            'full_name',
            'email',
            'message'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'متن پیام',
                'rows': '5'
            }),
        }
        labels = {
            'subject': 'موضوع',
            'email':'ایمیل',
            'full_name':'نام و نام خانوادگی',
            'message':'متن پیام',
        }
        