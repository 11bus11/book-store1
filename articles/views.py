from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Article
from .forms import ArticleForm


def articles(request):
    """view that shows articles"""

    articles = Article.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)


def article_full(request, article_id):
    """view that shows the full article."""

    article = get_object_or_404(Article, pk=article_id)

    context = {
            'article': article,
        }

    return render(request, 'articles/article_full.html', context)

def add_articles(request):
    """ Adding a product to store (admin)"""
    form = ArticleForm()
    template = 'articles/add:articles.html'
    context = {
        'form': form,
    }

    return render(request, template, context)