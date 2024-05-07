from django.db import models
from main.models import Car, CustomUser


class ProposalStatusEnum(models.TextChoices):
    CREATED = 'Создано'
    IN_PROCESS = 'В обработке'
    COMPLETED = 'Завершено'
    REFUSED = 'Отклонено'


class Proposal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    date_start = models.CharField(max_length=255, verbose_name="Дата начала")
    date_end = models.CharField(max_length=255, verbose_name="Дата окончания")
    total_price = models.IntegerField(verbose_name="Цена аренды")
    status = models.CharField(
        choices=ProposalStatusEnum.choices,
        default=ProposalStatusEnum.CREATED,
        max_length=32,
        verbose_name="Статус аренды"
    )

    
    def __str__(self) -> str:
        return f"#{self.id} {self.user.login} заказал {self.car.manufacturer} {self.car.name} на сумму {self.total_price}"


    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"