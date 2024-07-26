from django.db import models
from datetime import datetime
# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, blank=True)
    Caption = models.CharField(max_length=100)