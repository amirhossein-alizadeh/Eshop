from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from user_panel.forms import EditProfileModelForm


class UserPanelView(TemplateView):
    template_name = "user_panel/user_panel.html"



class EditProfileView(View):
    def get(self, request):
        edit_profile_form = EditProfileModelForm()
        context = {
            "form": edit_profile_form
        }
        return render(request, template_name="user_panel/edit_profile.html", context=context)


def panel_component(request):
    return render(request, template_name="user_panel/components/user_panel_component.html")
