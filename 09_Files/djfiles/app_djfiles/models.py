
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_("Название"))
    description = models.CharField(max_length=1000, verbose_name=_("Содрежание"), default='')
    created_at = models.DateTimeField(verbose_name=_("Дата создания"), auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=_("Дата редактирования"), auto_now=True)

    class Meta:
        verbose_name_plural = _('блог')
        verbose_name = _('блог')

class File(models.Model):
    file = models.FileField(verbose_name=_("Изображение"), default=None, upload_to='files/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _('файлы')
        verbose_name = _('файл')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0, validators=[MinValueValidator(1111111111), MaxValueValidator(9999999999)])
    city = models.CharField(max_length=20, blank=True)
    verification = models.BooleanField(default=False)
    avatar = models.ImageField(default=None, upload_to='files/')

    class Meta:
        verbose_name_plural = _('профили')
        verbose_name = _('профиль')

