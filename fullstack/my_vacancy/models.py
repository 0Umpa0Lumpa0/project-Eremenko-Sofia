from django.db import models


class MainInfo(models.Model):
    data = models.TextField(blank=True, verbose_name='Текст описания')
    photo = models.ImageField(upload_to='admin_data/%Y/%m/%d', blank=False, verbose_name='Фото профессии')

    def __str__(self):
        return 'Главная страница'


class JobDemand(models.Model):
    salary_level_chart = models.ImageField(upload_to='admin_data/%Y/%m/%d', blank=False,
                                           verbose_name='График уровень зарплат по годам')
    vacancy_count_chart = models.ImageField(upload_to='admin_data/%Y/%m/%d', blank=False,
                                            verbose_name='График количество вакансий по годам')
    data_table = models.TextField(blank=False, verbose_name='Таблица')

    def __str__(self):
        return 'Востребованность'
