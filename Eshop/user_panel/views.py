from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from user_panel.forms import EditProfileModelForm, ChangePasswordForm
from account.models import User


class UserPanelView(TemplateView):
    template_name = "user_panel/user_panel.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["user"] = User.objects.filter(id=self.request.user.id).first()
        return data


class EditProfileView(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile_form = EditProfileModelForm(instance=current_user)
        context = {
            "form": edit_profile_form,
            "current_user": current_user,
        }
        return render(request, template_name="user_panel/edit_profile.html", context=context)

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
        context = {
            "form": edit_profile_form,
            "current_user": current_user,
        }
        return render(request, template_name="user_panel/edit_profile.html", context=context)


class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        context = {
            "form": ChangePasswordForm()
        }

        return render(request, "user_panel/change_password.html", context)

    def post(self, request: HttpRequest):
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            current_password = change_password_form.cleaned_data.get("current_password")
            if current_user.check_password(current_password):
                new_password = change_password_form.cleaned_data.get("new_password")
                current_user.set_password(new_password)
                current_user.save()
                return redirect(reverse("login"))
            else:
                change_password_form.add_error(field="current_password", error="رمز عبور فعلی صحیح نمیباشد")

        context = {
            "form": change_password_form
        }
        return render(request, "user_panel/change_password.html", context)


def panel_component(request):
    return render(request, template_name="user_panel/components/user_panel_component.html")
