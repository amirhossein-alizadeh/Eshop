from unicodedata import category

from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles_list"),
    path("cat/<str:category>", ArticleListView.as_view(), name="articles_list_by_category"),
    path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
]
