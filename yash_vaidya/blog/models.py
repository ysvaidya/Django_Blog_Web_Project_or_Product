from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class blog_post(models.Model):

    STATUS_CHOICES = [
        ('draft','Draft'),
        ('published', 'Published')
    ]

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # It help to create user friendly urls bast on title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    


