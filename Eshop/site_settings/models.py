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
    