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


class CityStatistics(models.Model):
    salary_level_chart = models.ImageField(upload_to='admin_data/salary_level/%Y/%m/%d', blank=False,
                                           verbose_name='График уровня зарплаты по городам')
    vacancy_fraction_chart = models.ImageField(upload_to='admin_data/vacancy_fraction/%Y/%m/%d', blank=False,
                                               verbose_name='График доли вакансий по городам')
    statistics_table = models.TextField(blank=False, verbose_name='Таблица статистики')

    def __str__(self):
        return 'География'


class SkillSet(models.Model):
    header_table = models.TextField(blank=False, verbose_name='Название таблицы', max_length=30)
    table = models.TextField(blank=False, verbose_name='Таблица')
    graph = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График по скиллам')

    def __str__(self):
        return 'Навыки'


class RecentVacancies(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок работы')
    content_to_parse = models.TextField(blank=False, verbose_name='Текст вакансии для парсинга', max_length=15)

    def __str__(self):
        return 'Последние вакансии'
