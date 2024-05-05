from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article.models import Article


# Create your views here.
class articles_list(ListView):
    model = Article
    template_name = "main/pages/articles.html"
    context_object_name = "articles"
    paginate_by = 2


class article_detail(DetailView):
    model = Article
    template_name = "main/pages/article_detail.html"
    context_object_name = "article"
