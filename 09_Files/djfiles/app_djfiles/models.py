
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Blog(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Название")
    description = models.CharField(max_length=1000, verbose_name="Содрежание", default='')
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)

class File(models.Model):
    file = models.FileField(verbose_name="Изображение", default=None, upload_to='files/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0, validators=[MinValueValidator(1111111111), MaxValueValidator(9999999999)])
    city = models.CharField(max_length=20, blank=True)
    verification = models.BooleanField(default=False)
    avatar = models.ImageField(default=None, upload_to='files/')
