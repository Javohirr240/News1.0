from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Drafted = 'DF', 'Draft'
        Published = 'PB', 'Publish'
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='news/images', null=True, blank=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices= Status.choices,
        default=Status.Drafted,
    )

    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager

    class Meta:
        ordering = ['-published_time']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detailview', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE , related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created_time']
    def __str__(self):
        return self.body