from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان", db_index=True)
    title_in_url = models.CharField(
        max_length=300,
        verbose_name="عنوان در url",
        db_index=True
    )
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=False)
    is_delete = models.BooleanField(verbose_name="حذف شده / نشده", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")
    category = models.ManyToManyField(
        to=ProductCategory,
        verbose_name="دسته بندی",
        related_name="products"
    )
    short_description = models.CharField(
        verbose_name="توضیحات کوتاه",
        max_length=512,
        db_index=True
    )
    full_description = models.TextField(verbose_name="توضیحات اصلی")
    slug = models.SlugField(default="", null=False, verbose_name="اسلاگ")
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=False)
    is_delete = models.BooleanField(verbose_name="حذف شده / نشده", default=False)
    
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


class ProductTag(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان", db_index=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="محصول", related_name="product_tags")
    
    class Meta:
        verbose_name = "تگ محصول"
        verbose_name_plural = "تگ های محصولات"

    def __str__(self):
        return self.title
