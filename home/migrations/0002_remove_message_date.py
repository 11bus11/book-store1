# Generated by Django 3.2 on 2023-01-06 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date',
        ),
    ]