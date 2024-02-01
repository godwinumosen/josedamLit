# Generated by Django 5.0.1 on 2024-01-27 20:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0004_teams'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constructionpost',
            options={'ordering': ['-publish_date1']},
        ),
        migrations.AlterModelOptions(
            name='teams',
            options={'ordering': ['-publish_date']},
        ),
        migrations.RenameField(
            model_name='constructionpost',
            old_name='publish_date',
            new_name='publish_date1',
        ),
        migrations.AddField(
            model_name='teams',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]