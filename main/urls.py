from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:id>/', views.article_detail, name='articles_page')
]
