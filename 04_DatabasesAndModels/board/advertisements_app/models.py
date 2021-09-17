from django.db import models

from django.db import models
import datetime

# Create your models here.

def close_date_time():
    now = datetime.datetime.now()
    return now + datetime.timedelta(days=1)


class Advertisements(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=1000, db_index=True)
    description = models.TextField(verbose_name='Описание', max_length=1000, default='')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    close_date = models.DateTimeField(verbose_name="Дата окончания публикации", default=close_date_time())
    price = models.FloatField(verbose_name="Цена", default=0)
    views_count = models.IntegerField(verbose_name="Количество просмотров", default=0)
    status = models.ForeignKey('AdvertisementsStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name="advertisements", verbose_name="Статус")
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name="type", verbose_name="Тип объявления")
    author = models.ForeignKey('AdvertisementAuthor', verbose_name="Автор", default=None, null=True,
                               on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey('AdvertisementCategory', verbose_name="Рубрика", default=None, null=True,
                                 related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementsStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name="Статус")

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип объявления")

    def __str__(self):
        return self.name

class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(max_length=150, verbose_name="Электронная почта", default='')
    phone_number = models.IntegerField(max_length=11, verbose_name="Номер телефона")

    def __str__(self):
        return self.name

class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Рубрика")

    def __str__(self):
        return self.name