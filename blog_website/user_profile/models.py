from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustumeUserManager
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        max_length=150,
        unique=True,
        error_messages={'unique': 'A user with that email already exists.'}
    )
    profile_image = models.ImageField(null=True, upload_to='profile_image' , blank=True)
    
    REQUIRED_FIELDS =['email']
    objects = CustumeUserManager()
    
    def __str__(self) -> str:
        return self.username