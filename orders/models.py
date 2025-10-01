from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Order(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новый'
        IN_PROGRESS = 'in_progress', 'В работе'
        PENDING = 'under approval', 'На согласовании'
        PARTS_SEARCH = 'parts_search', 'Поиск запчасти'
        READY = 'ready', 'Готов'
        CLOSED = 'closed', 'Закрыт'

    # number = models.IntegerField(unique=True, verbose_name="Номер заказа")
    number_order = models.AutoField(primary_key=True, verbose_name='Номер заказа')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW, verbose_name='Статус заказа')
    priority = models.BooleanField(default=False, verbose_name="Приоритет")
    client_name = models.CharField(max_length=55, verbose_name=_('ФИО'), default="Хулиана Ульяна Яковлева")
    client_phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    client_address = models.TextField(verbose_name='Адрес')
    device_model = models.CharField(max_length=70, verbose_name='Бытовая техника')
    problem_description = models.TextField(verbose_name='Поломка')
    assigned_to = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Менеджер')
    price_estimate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Стоимость начальная')
    final_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Стоимость финальная')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменён')
    # deleted = models.BooleanField(default=False, verbose_name="Удален")
    watch_count = models.IntegerField(default=0, verbose_name="Количество просмотров заявки")

    def __str__(self):
        # return f"Заказ # {self.number} - {self.client_name}"
        return f"Заказ № {self.number_order}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"