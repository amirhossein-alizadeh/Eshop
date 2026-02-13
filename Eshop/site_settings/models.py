from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    site_title = models.CharField(
        max_length=300,
        verbose_name="نام سایت"
    )
    site_domain = models.CharField(
        max_length=300,
        verbose_name="دامنه سایت"
    )
    site_logo = models.ImageField(
        verbose_name="لوگو سایت",
        upload_to="images/site_settings"
    )
    about_us_text = models.TextField(verbose_name="متن درباره ما")
    address = models.CharField(
        max_length=400,
        verbose_name="آدرس",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="تلفن"
    )
    fax = models.CharField(
        max_length=20,
        verbose_name="فکس"
    )
    email = models.EmailField(
        max_length=100,
        verbose_name="ایمیل"
    )
    copyright_text = models.CharField(
        max_length=300,
        verbose_name="متن کپی رایت"
    )
    is_main_setting = models.BooleanField(verbose_name="تنظیمات اصلی")
    
    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات"
        
    def __str__(self):
        return self.site_title
    
    
class FooterLinkBox(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="عنوان"
    )
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    
    class Meta:
        verbose_name = "دسته بندی لینک های فوتر"
        verbose_name_plural = "دسته بندی های لینک های فوتر"
        
    def __str__(self):
        return self.title



class FooterLink(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="عنوان"
    )
    url = models.URLField(
        max_length=500,
        verbose_name="لینک"
    )
    footer_link_box = models.ForeignKey(
        to=FooterLinkBox,
        on_delete=models.CASCADE,
        verbose_name="دسته بندی",
        related_name="links"
    )
    
    class Meta:
        verbose_name = "لینک فوتر"
        verbose_name_plural = "لینک های فوتر"
        
    def __str__(self):
        return self.title
    
    
class Slider(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    url = models.URLField(max_length=500, verbose_name="لینک")
    url_title = models.CharField(max_length=300, verbose_name="عنوان لینک")
    
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="images/sliders", verbose_name="تصویر اسلایدر")
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)
    
    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"
        
    def __str__(self):
        return self.title


class CommercialBanner(models.Model):
    title = models.CharField(max_length=125, verbose_name="عنوان")
    url = models.URLField(max_length=512, verbose_name="URL", null=True, blank=True)
    image = models.ImageField(upload_to="images/banners", verbose_name="تصویر بنر")
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    is_deleted = models.BooleanField(verbose_name="حذف شده / نشده")

    class Meta:
        verbose_name = "بنر تبلیغاتی"
        verbose_name_plural = "بنر های تبلیغاتی"

    def __str__(self):
        return self.title