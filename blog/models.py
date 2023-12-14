from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Пост')
    slug = models.CharField(max_length=200, verbose_name='Ссылка', **NULLABLE)
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    views_count = models.IntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
