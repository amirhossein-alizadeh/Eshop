from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_settings.models import FooterLinkBox, SiteSettings

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home_index.html'
    
def header_component(request):
    site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
    return render(
        request=request, 
        template_name="shared/site_header_component.html",
        context={
            "site_settings": site_settings
        }
    )


def footer_component(request):
    site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    return render(
        request=request, 
        template_name="shared/site_footer_component.html",
        context={
            "site_settings": site_settings,
            "footer_link_boxes": footer_link_boxes
        }
    )
    
    
class AboutUsView(TemplateView):
    template_name = "home/about_us.html"
    
    def get_context_data(self, **kwargs):
        site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
        context = super().get_context_data(**kwargs)
        context["site_settings"] = site_settings
        return context
    