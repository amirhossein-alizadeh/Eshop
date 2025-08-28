from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .forms import ForgotPasswordForm, LoginForm, RegisterForm, ResetPasswordForm
from .models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from utils.email_service import send_email

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
                send_email(
                    subject="فعال سازی حساب کاربری",
                    to=new_user.email,
                    context={
                        "user": new_user
                        },
                    template_name="email/activate_account.html"
                )
                return redirect(reverse("login"))
                
            
        return render(
            request=request,
            template_name="account/register.html",
            context={
                "register_form":register_form
            }
        )
            
            
class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(
            request=request,
            template_name="account/login.html",
            context={
                "login_form":login_form
            }
        )
        
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            
            user_email = login_form.cleaned_data.get("email")
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user:
                user_pass = login_form.cleaned_data.get("password")
                password_correct = user.check_password(user_pass)
                if password_correct:
                    login(
                        request=request,
                        user=user
                    )
                    return redirect(reverse("home"))
                else:
                    login_form.add_error(
                        field="email",
                        error="ایمیل یا رمز وارد شده نادرست است"
                    )
            else:
                login_form.add_error(
                    field="email",
                    error="ایمیل یا رمز وارد شده نادرست است"
                )
        return render(
            request=request,
            template_name="account/login.html",
            context={
                "login_form": login_form
            }
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
        
        
class ForgotPasswordView(View):
    def get(self, request: HttpRequest):
        forgot_pass_form = ForgotPasswordForm()
        return render(
            request=request,
            template_name="account/forget_password.html",
            context={
                "forgot_pass_form": forgot_pass_form
            }
        )
        
    def post(self, request: HttpRequest):
        
        forgot_pass_form = ForgotPasswordForm(request.POST)
        
        if forgot_pass_form.is_valid():
            email = forgot_pass_form.cleaned_data.get("email")
            user:User = User.objects.filter(email__iexact=email).first()
            if user:
                if user.is_active:
                    send_email(
                        subject="بازیابی کلمه عبور",
                        to=user.email,
                        context={
                            "user":user
                        },
                        template_name="email/forgot_password.html"
                    )
                    return redirect(reverse("login"))
            
            forgot_pass_form.add_error(
                field="email",
                error="ایمیل وارد شده در سیستم وجود ندارد"
            )         
        
        return render(
            request=request,
            template_name="account/forget_password.html",
            context={
                "forgot_pass_form": forgot_pass_form
            }
        )
        
    
class ResetPasswordView(View):
    def get(self, request: HttpRequest, email_active_code):
        user : User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user:
            reset_pass_form = ResetPasswordForm()
        
            return render(
                request=request,
                template_name="account/reset_password.html",
                context={
                    "reset_pass_form": reset_pass_form,
                    "user":user
                }
            )
        raise Http404
    
    def post(self, request:HttpRequest, email_active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        if reset_pass_form.is_valid():
            user : User = User.objects.filter(email_active_code__iexact=email_active_code).first()
            if user:
                if user.is_active:
                    password = reset_pass_form.cleaned_data.get("password")
                    user.set_password(password)
                    user.email_active_code = get_random_string(128)
                    user.save()
                    return redirect(reverse("login"))
            
            raise Http404
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("login"))