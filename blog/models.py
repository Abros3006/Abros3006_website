from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.title