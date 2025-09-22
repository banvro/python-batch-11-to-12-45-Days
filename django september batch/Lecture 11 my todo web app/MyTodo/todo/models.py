from django.db import models

# Create your models here.

class myTodo(models.Model):
    title = models.CharField(max_length=100)
    dexription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    