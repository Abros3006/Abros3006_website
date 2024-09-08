from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    Date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.CharField(max_length=100000)