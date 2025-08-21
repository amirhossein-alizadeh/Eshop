from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from .models import User

# Create your views here.
class RegisterView(View):
    
    def get(self, request):
        register_form = RegisterForm()
        return render(
            request=request,
            template_name='account/register.html',
            context={
                "register_form": register_form
            }
        )
        
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get("email")
            