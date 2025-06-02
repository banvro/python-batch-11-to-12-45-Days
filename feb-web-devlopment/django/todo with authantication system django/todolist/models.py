from django.db import models

# Create your models here.

class addtodo(models.Model):
    ta_sk = models.CharField(max_length=50)
    descri_ption = models.TextField()