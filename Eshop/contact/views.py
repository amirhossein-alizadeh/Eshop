from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView
from .forms import ContactUsModelForm

# Create your views here.

class ContactUsFormView(FormView):
    template_name = 'contact/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    