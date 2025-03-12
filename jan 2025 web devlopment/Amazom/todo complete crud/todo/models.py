from django.db import models

# Create your models here.

class mytodo(models.Model):
    title = models.CharField(max_length=150)
    discption = models.TextField()