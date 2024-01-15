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
    date = models.DateField(blank=True, verbose_name='Дата парсинга')

    def __str__(self):
        return 'Последние вакансии'


class Navigations(models.Model):
    vacancy_title = models.TextField(blank=False, verbose_name='Заголовок вакансии', max_length=100)
    logo_image = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='Логотип')
    first_menu_item = models.TextField(blank=False, verbose_name='Первый пункт меню', max_length=25)
    second_menu_item = models.TextField(blank=False, verbose_name='Второй пункт меню', max_length=25)
    third_menu_item = models.TextField(blank=False, verbose_name='Третий пункт меню', max_length=25)
    fourth_menu_item = models.TextField(blank=False, verbose_name='Четвертый пункт меню', max_length=25)
    fifth_menu_item = models.TextField(blank=False, verbose_name='Пятый пункт меню', max_length=25)
    author_name = models.TextField(blank=False, verbose_name='Автор', max_length=50)

    def __str__(self):
        return 'Навигация'
