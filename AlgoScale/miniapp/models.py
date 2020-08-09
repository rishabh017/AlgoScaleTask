from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField(max_length=200)
    hometown=models.CharField(max_length=200)
