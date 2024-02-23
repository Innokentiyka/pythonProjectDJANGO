from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    view_count = models.IntegerField(default=0)
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title