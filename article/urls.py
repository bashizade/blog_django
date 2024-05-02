from django.urls import path
from article import views

urlpatterns = [
    path('list/', views.articles_list.as_view(), name="article_list")
]
