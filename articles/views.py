from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Article
#from .forms import ProductForm


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
