# Generated by Django 3.2 on 2022-12-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_place',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
