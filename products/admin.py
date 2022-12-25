from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'author',
        'language',
        'price',
        'stock',
        'description',
        'image',
    )

    ordering = (
        'name',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)