from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
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
    class Meta:
        ordering = ['-published_time']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detailview', kwargs={'slug': self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name