# Generated by Django 4.1.13 on 2025-03-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
