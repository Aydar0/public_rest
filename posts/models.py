from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=50)
    body = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(verbose_name='Create', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return self.title
        