from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Article, ArticleCategory


class ArticleListView(ListView):
    template_name = "articles/articles_list.html"
    model = Article
    context_object_name = "articles"
    paginate_by = 1
    def get_queryset(self):
        query_set = super(ArticleListView, self).get_queryset()
        category = self.kwargs.get("category")
        if category:
            category = self.kwargs.get("category")
            if category:
                query_set = query_set.filter(categories__url_title__iexact=category)
        return query_set


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    model = Article
    context_object_name = "article"
    def get_queryset(self):
        query_set = super(ArticleDetailView, self).get_queryset()
        query = query_set.filter(is_active=True)
        return query


def article_categories_component(request):
    article_catgories = ArticleCategory.objects.filter(is_active=True, parent__id__iexact=None).all()
    context = {
        "article_catgories": article_catgories,
    }

    return render(request=request,
                  template_name="articles/components/article_categories_list.html",
                  context=context)
