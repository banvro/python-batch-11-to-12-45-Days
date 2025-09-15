from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email_address = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return f"Username is : {self.full_name} and phon number is {self.phone_number}"


choice = [
    ("Frontend Devloper", "Frontend Devloper"),
    ("Backend Devloper", "Backend Devloper"),
    ("Tester", "Tester")
    ]

class Employee(models.Model):
    e_name = models.CharField(max_length=50)
    e_branch = models.CharField(max_length=50, choices = choice, default = "Backend Devloper")
    e_p_num = models.IntegerField()