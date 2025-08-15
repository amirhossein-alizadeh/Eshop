from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

# Create your views here.

class ContactUsPage(View):
    def get(self, request):
        return render(request=request, template_name='contact/contact_us_page.html', context={})
    
    def post(self, request):
        email = request.POST['email']
        name = request.POST['name']
        
        print(email)
        print(name)
        return redirect(reverse('home'))