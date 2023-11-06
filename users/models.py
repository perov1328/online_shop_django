from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE

# Create your models here.

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    verified = models.BooleanField(default=False, verbose_name='Активация')
    verification_code = models.IntegerField(default=0, verbose_name='Код верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
