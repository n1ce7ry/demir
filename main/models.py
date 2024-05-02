from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(AbstractUser):
    login = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name="Логин")
    passport_details = models.CharField(max_length=10, null=True, blank=True, verbose_name="Паспортные данные")
    phone = models.CharField(max_length=12, null=True, blank=True, verbose_name="Номер телефона")
    fio = models.CharField(max_length=255, verbose_name="ФИО")


class Tag(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Car(models.Model):
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    name = models.CharField(max_length=255, verbose_name='Наименование авто')
    run = models.CharField(max_length=255, verbose_name="Пробег")
    price = models.IntegerField(verbose_name='Цена в тыс/руб')
    image = models.ImageField(upload_to="cars/")
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"