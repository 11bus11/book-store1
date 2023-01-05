from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import MessageForm
from .models import Message

# Create your views here.


def index(request):
    """view that returns index page"""

    message_form = MessageForm()
    template = 'home/index.html'
    context = {
        'message_form': message_form,
    }

    return render(request, template, context)

def messages(request):
    """view that shows the full article."""

    message = Message.message

    context = {
            'message': message,
        }

    return render(request, 'home/messages.html', context)