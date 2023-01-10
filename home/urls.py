from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('send_messages/', views.send_message, name='send_messages'),
    path('message/', views.message_view, name='message'),
]
