from django.db import models

SCORE_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    language = models.CharField(max_length=255, default='Svenska')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_place = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'

    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.CASCADE)
    score = models.IntegerField(choices=SCORE_CHOICES, default=4)
    name = models.CharField(max_length=254)

    def __name__(self):
        return self.name