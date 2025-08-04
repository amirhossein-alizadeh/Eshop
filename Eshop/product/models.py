from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class ProductTag(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    
    class Meta:
        verbose_name = "تگ محصول"
        verbose_name_plural = "تگ های محصولات"

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    title_in_url = models.CharField(
        max_length=300, verbose_name="عنوان در url", null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")
    category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
        verbose_name="دسته بندی",
        null=True,
        related_name="products"
    )
    product_tags = models.ManyToManyField(ProductTag, verbose_name="تگ های محصول", related_name="products")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1,
        verbose_name="امتیاز",
    )
    short_description = models.CharField(
        verbose_name="توضیحات کوتاه", max_length=512, null=True
    )
    slug = models.SlugField(default="", null=False, db_index=True, verbose_name="اسلاگ")
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
