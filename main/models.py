from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(AbstractUser):
    login = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name="Логин")
    passport_details = models.CharField(max_length=10, null=True, blank=True, verbose_name="Паспортные данные")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="Номер телефона")