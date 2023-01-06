from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>', views.article_full, name='article_full'),
    path('add/', views.add_articles, name='add_articles'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_articles'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_articles')
]