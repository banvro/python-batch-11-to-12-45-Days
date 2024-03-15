from django.db import models

# Create your models here.

class MyTodo(models.Model):
    todo_title = models.CharField(max_length=150)
    todo_desc = models.TextField()
    date =  models.DateField(auto_now_add=True)