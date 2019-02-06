from django.db import models

class Post(models.Model):
    theme = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateField()
# Create your models here.
