from django.db import models

# Create your models here.


class ArticleCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    url_title = models.CharField(max_length=300, verbose_name="عنوان در URL", unique=True)
    parent = models.ForeignKey(
        to='ArticleCategory',
        on_delete=models.CASCADE,
        verbose_name="دسته بندی والد",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "دسته بندی مقالات"
        verbose_name_plural = "دسته بندی های مقالات"
        

class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    slug = models.SlugField(
        max_length=400,
        verbose_name="اسلاگ",
        db_index=True,
        allow_unicode=True
    )
    image = models.ImageField(upload_to="images/articles", verbose_name="تصویر مقاله")
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    text = models.TextField(verbose_name="متن کامل مقاله")
    categories = models.ManyToManyField(to=ArticleCategory, verbose_name="دسته بندی ها", related_name="articles")
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        
        
    def __str__(self):
        return self.title