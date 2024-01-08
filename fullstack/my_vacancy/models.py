from django.db import models


class MainInfo(models.Model):
    data = models.TextField(blank=True, verbose_name='Текст описания')
    photo = models.ImageField(upload_to='admin_data/%Y/%m/%d', blank=False, verbose_name='Фото профессии')

    def __str__(self):
        return 'Главная страница'
