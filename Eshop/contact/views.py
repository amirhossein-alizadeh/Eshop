from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .forms import ContactUsModelForm

# Create your views here.

class ContactUsPage(View):
    def get(self, request):
        contact_us_form = ContactUsModelForm()
        return render(
            request=request,
            template_name='contact/contact_us_page.html',
            context={'contact_us_form': contact_us_form}
        )
    
    def post(self, request):
        contact_us_form = ContactUsModelForm(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            return redirect(reverse('home'))
        return render(
            request=request,
            template_name='contact/contact_us_page.html',
            context={'contact_us_form': contact_us_form}
        )