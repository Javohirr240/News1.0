from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    avatar = models.ImageField(upload_to='accounts.images', null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} Profile"
