from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category
#from .forms import ProductForm


def all_products(request):
    """view that shows products (sorting and search too)"""
    products = Product.objects.all()
    return render(request, 'products/products.html')
