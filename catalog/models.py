from typing import Optional
from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название категории')
    category_description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название товара')
    product_description = models.TextField(verbose_name='Описание товара')
    preview_icon = models.ImageField(upload_to='catalog/', blank=True, null=True, verbose_name='Превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    price = models.FloatField(verbose_name='Цена за шт.')
    data_created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    data_modified = models.DateField(verbose_name='Дата изменения', auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Автор')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return f'{self.product_name}'

    @property
    def active_version(self) -> Optional['Version']:
        return self.version_set.filter(is_active=True).last()

    class Meta:
        verbose_name = 'Товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Товары'  # Настройка для наименования набора объектов


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_version = models.IntegerField(verbose_name="Номер версии")
    name_version = models.CharField(max_length=100, verbose_name="Название версии")
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.name_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
