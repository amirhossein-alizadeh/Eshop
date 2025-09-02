from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView

from site_settings.models import SiteSettings
from .forms import ContactUsModelForm

# Create your views here.

class ContactUsFormView(FormView):
    template_name = 'contact/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
        context["site_settings"] = site_settings
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    