from django.db import models


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

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Товары'  # Настройка для наименования набора объектов
