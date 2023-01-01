# Generated by Django 3.2 on 2023-01-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=3000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
