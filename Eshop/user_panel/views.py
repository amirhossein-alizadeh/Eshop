from django.shortcuts import render
from django.views import View
from user_panel.forms import EditProfileModelForm


# Create your views here.

class EditProfileView(View):
    def get(self, request):
        edit_profile_form = EditProfileModelForm()
        context = {
            "form": edit_profile_form
        }
        return render(request, template_name="user_panel/edit_profile.html", context=context)