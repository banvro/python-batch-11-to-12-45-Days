from django.db import models
 
# Create your models here.
# id

class ContactUs(models.Model):
    username = models.CharField(max_length=150)
    useremail = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    message = models.TextField()
    myimage = models.ImageField(upload_to = "userprofile", null = True, blank = True)
    
