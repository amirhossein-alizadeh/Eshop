from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from user_panel.forms import EditProfileModelForm
from account.models import User


class UserPanelView(TemplateView):
    template_name = "user_panel/user_panel.html"


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
        edit_profile_form = EditProfileModelForm(request.POST,request.FILES, instance=current_user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
        context = {
            "form": edit_profile_form,
            "current_user": current_user,
        }
        return render(request, template_name="user_panel/edit_profile.html", context=context)

def panel_component(request):
    return render(request, template_name="user_panel/components/user_panel_component.html")
