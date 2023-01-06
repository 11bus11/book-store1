from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_products'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_products'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_products'),
    path('reviews/', views.review, name='reviews'),
]
