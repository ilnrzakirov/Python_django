from django.db import models

# Create your models here.

class Advertisements(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=1000, db_index=True)
    description = models.TextField(verbose_name='Описание', max_length=1000, default='')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    price = models.FloatField(verbose_name="Цена", default=0)
    views_count = models.IntegerField(verbose_name="Количество просмотров", default=0)
    status = models.ForeignKey('AdvertisementsStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name="advertisements", verbose_name="Статус")
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name="type", verbose_name="Тип объявления")

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