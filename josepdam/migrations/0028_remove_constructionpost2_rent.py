# Generated by Django 5.0.1 on 2024-02-29 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0027_constructionpost2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructionpost2',
            name='rent',
        ),
    ]