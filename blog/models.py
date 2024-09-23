from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    para1heading = models.CharField(max_length=100, blank=True)
    para1 = models.TextField(default='para1', blank=True)
    para2heading = models.CharField(max_length=100, blank=True)
    para2 = models.TextField(default='para2', blank=True)
    para3heading = models.CharField(max_length=100, blank=True)
    para3 = models.TextField(default='para3', blank=True)
    para4heading = models.CharField(max_length=100, blank=True)
    para4 = models.TextField(default='para4', blank=True)
    para5heading = models.CharField(max_length=100, blank=True)
    para5 = models.TextField(default='para5', blank=True)
    para6heading = models.CharField(max_length=100, blank=True)
    para6 = models.TextField(default='para6', blank=True)
    para7heading = models.CharField(max_length=100, blank=True)
    para7 = models.TextField(default='para7', blank=True)
    para8heading = models.CharField(max_length=100, blank=True)
    para8 = models.TextField(default='para8', blank=True)
    para9heading = models.CharField(max_length=100, blank=True)
    para9 = models.TextField(default='para9', blank=True)
    para10heading = models.CharField(max_length=100, blank=True)
    para10 = models.TextField(default='para10', blank=True)

    def __str__(self):
        return self.title