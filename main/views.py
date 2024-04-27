from django.shortcuts import render

from article.models import Article


# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request, 'main/pages/home.html', {'articles': articles})


def articles_page(request):
    articles = Article.objects.all()
    return render(request, 'main/pages/articles.html', {'articles': articles})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'main/pages/article_detail.html', {'article': article})
