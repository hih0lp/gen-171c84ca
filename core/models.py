from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В работе'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменен'),
    ]
    
    customer_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес доставки')
    order_details = models.TextField(verbose_name='Состав заказа')
    desired_datetime = models.DateTimeField(verbose_name='Желаемые дата/время')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Заказ #{self.id} от {self.customer_name}'