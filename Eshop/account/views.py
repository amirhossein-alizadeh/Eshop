from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .forms import RegisterForm
from .models import User
from django.utils.crypto import get_random_string

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
            if User.objects.filter(email__iexact = email).exists():#todo this is mistake
                register_form.add_error(
                    field="email",
                    error="ایمیل وارد شده قبلا در سایت ثبت شده است"
                )
            else:
                password = register_form.cleaned_data.get("password")
                email_active_code = get_random_string(128)
            
                new_user = User(
                    username = email,
                    email=email,
                    email_active_code=email_active_code,
                    is_active=False
                )
                new_user.set_password(password)
                new_user.save()
                return redirect(reverse("login"))
                #TODO: send activation email
            
            return render(
                request=request,
                template_name="account/register.html",
                context={
                    "register_form":register_form
                }
            )
            
            
class LoginView(View):
    def get(self, request):
        return render(
            request=request,
            template_name="account/login.html",
            context={}
        )
        
        
class ActivateAccount(View):
    def get(self, request, activate_code):
        
        user: User = User.objects.filter(email_active_code=activate_code).first()
        
        if user:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(128)
                user.save()
                return redirect(reverse("login"))
            else:
                #TODO show your account already activated
                pass
        else:
            raise Http404