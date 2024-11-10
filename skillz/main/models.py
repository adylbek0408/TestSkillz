from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название круса', help_text='Введите название курса')
    author = models.CharField(max_length=155, verbose_name='Автор курса')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Картинка')
    description = models.TextField(verbose_name='Описание')
    city = models.CharField(verbose_name='Адрес')
    created_date = models.DateField(verbose_name='Дата создание')
    updated_date = models.DateTimeField(verbose_name='Дата обновлении')


class Article(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курсы', related_name='article_course')
    new_price = models.FloatField(verbose_name='Цена')
    created_date = models.DateField(verbose_name='Дата создание')
    updated_date = models.DateTimeField(verbose_name='Дата обновлении')


class FreeWorkshops(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_date = models.DateField(verbose_name='Дата создание')

