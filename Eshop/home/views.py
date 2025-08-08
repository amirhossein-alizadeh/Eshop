from django.shortcuts import render
from django.views import View

# Create your views here.
class home(View):
    
    def get(self, request):
        return render(request=request, template_name="home/home_index.html")
    
def header_component(request):
    return render(request=request, template_name="shared/site_header_component.html")


def footer_component(request):
    return render(request=request, template_name="shared/site_footer_component.html")