from django.contrib import admin

from .models import ArticleCategory, Article

# Register your models here.
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "url_title",
        "parent",
        "is_active"
    ]
    list_editable = ["is_active"]
    list_filter = ["is_active"]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)

admin.site.register(Article)