from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm

# Create your views here.


def index(request):
    """view that returns index page"""

    contact_form = ContactForm()
    template = 'home/index.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)

