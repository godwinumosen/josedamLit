# Generated by Django 5.0.1 on 2024-02-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0012_constructionpost_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionpost',
            name='qm',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constructionpost',
            name='rent',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]