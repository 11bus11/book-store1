from django.contrib import admin
from .models import Product, Category, Review


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'score',
        'name',
    )

    ordering = (
        'score',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)