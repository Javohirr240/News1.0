# Generated by Django 4.1.13 on 2025-03-08 17:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/images')),
                ('body', models.TextField()),
                ('published_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Publish')], default='DF', max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.category')),
            ],
        ),
    ]
