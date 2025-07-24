from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="نام")
    price = models.IntegerField(verbose_name="قیمت")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=0
    )
    
    def __str__(self):
        return f"{self.title}({self.price})"
    
    