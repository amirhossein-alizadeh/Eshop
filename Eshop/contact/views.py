from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .forms import ContactUsForm

# Create your views here.

class ContactUsPage(View):
    def get(self, request):
        contact_us_form = ContactUsForm()
        return render(
            request=request,
            template_name='contact/contact_us_page.html',
            context={'contact_us_form': contact_us_form}
        )
    
    def post(self, request):
        contact_us_form = ContactUsForm(request.POST)
        if contact_us_form.is_valid():
            print(contact_us_form.cleaned_data)
            return redirect(reverse('home'))