from django.contrib import admin

from .models import SiteSettings, FooterLinkBox, FooterLink, Slider, CommercialBanner

# Register your models here.

class CommercialBannerModelAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "is_active"]

admin.site.register(SiteSettings)
admin.site.register(FooterLinkBox)
admin.site.register(FooterLink)
admin.site.register(Slider)
admin.site.register(CommercialBanner, CommercialBannerModelAdmin)