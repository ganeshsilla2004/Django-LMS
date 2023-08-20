from django.db import models

# Create your models here.


class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    

class register(models.Model):
    id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
