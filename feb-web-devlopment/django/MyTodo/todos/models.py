from django.db import models
from datetime import datetime    

# Create your models here.

class mytodo(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    tododone = models.BooleanField(default = False)
    datetime = models.DateTimeField(auto_now_add=True, blank = True)