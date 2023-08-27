from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from CoreApp.manager import UserManager
from django.apps import apps


class CustomUser(AbstractBaseUser):
    username = None
    id_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100,default='')
    
    USERNAME_FIELD = 'id_no'
    REQUIRED_FIELDS = ['email'] 
    objects = UserManager()


