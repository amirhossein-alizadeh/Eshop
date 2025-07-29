from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="نام")
    price = models.IntegerField(verbose_name="قیمت")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=0
    )
    short_description = models.CharField(verbose_name="توضیحات کوتاه", max_length=512, null=True)
    slug = models.SlugField(default="", null=False, db_index=True)
    is_active = models.BooleanField(verbose_name="فعال/غیرفعال", default=False)
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})
    
    
    def __str__(self):
        return f"{self.title}({self.price})"
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"