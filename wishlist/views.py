from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product, Category
from .models import wishlist
# Create your views here.


def wishlist(request):
    """ A view that renders the wishlist contents page """
    return render(request, 'wishlist/wishlist.html')
