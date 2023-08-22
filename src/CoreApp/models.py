from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, id_no, email, password=None, **extra_fields):
        if not id_no:
            raise ValueError("The ID Number must be set")
        email = self.normalize_email(email)
        
        user = self.model(
            id_no=id_no,
            email=email,
            **extra_fields
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_no, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(id_no, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id_no = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'id_no'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.id_no
