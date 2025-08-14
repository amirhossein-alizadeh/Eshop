from django.db import models

# Create your models here.

class ContactUs(models.Model):
    subject = models.CharField(max_length=300, verbose_name='موضوع')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_data = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)