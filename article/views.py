from django.shortcuts import render
from django.views.generic import ListView

from article.models import Article


# Create your views here.
class articles_list(ListView):
    model = Article
    template_name = "main/pages/articles.html"
    context_object_name = "articles"
