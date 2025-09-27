from django.views.generic.list import ListView
from .models import Article


class ArticleListView(ListView):
    template_name = "articles/articles_list.html"
    model = Article
    context_object_name = "articles"
    paginate_by = 10