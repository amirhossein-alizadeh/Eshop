from django.shortcuts import render
from django.views.generic.base import TemplateView

from product.models import Product
from site_settings.models import FooterLinkBox, SiteSettings, Slider
from utils.convertors import group_list

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home_index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context["sliders"] = sliders
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by("-id")[:12]
        context["latest_products"] = group_list(latest_products)
        print(context["latest_products"])
        return context
    
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
    