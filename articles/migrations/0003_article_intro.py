# Generated by Django 3.2 on 2022-12-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='intro',
            field=models.CharField(default='testing  1', max_length=500),
            preserve_default=False,
        ),
    ]
