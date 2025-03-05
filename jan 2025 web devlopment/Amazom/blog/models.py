from django.db import models

# Create your models here.

class Contactinfo(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    message = models.TextField()

