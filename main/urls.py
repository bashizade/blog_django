from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles_page, name='articles_page'),
    path('articles/<int:id>/', views.articles_page, name='articles_page')
]
