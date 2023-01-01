from django.db import models


class Article(models.Model):

    class Meta:
        verbose_name_plural = 'Articles'

    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    intro = models.CharField(max_length=500)
    content = models.CharField(max_length=3000)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
