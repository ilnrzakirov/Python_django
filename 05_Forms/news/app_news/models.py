from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class NewsStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name="Флаг активности")

    def __str__(self):
        return self.status


class News(models.Model):
    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'inactive'),
        ('o', 'inspection'),
    ]
    name = models.CharField(max_length=1000, verbose_name="Название")
    description = models.CharField(max_length=1000, verbose_name="Содрежание", default='')
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='o')
    categories = models.ForeignKey('Categories', verbose_name='Категория', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} {self.created_at} {self.status}'

    class Meta:
        ordering = ['name']


class NewsComment(models.Model):
    username = models.CharField( default='Аноним',
                                 max_length=50, verbose_name="Имя пользователя")
    comment_text = models.CharField(max_length=1000, default='')
    news = models.ForeignKey('News', on_delete=models.CASCADE,  null=True, verbose_name="новость",
                             default=None)

    def __str__(self):
        return f'{self.id}. {self.username} {self.news} {self.comment_text}'

    def get_comment_text(self):
        if len(f'{self.comment_text}') > 15:
            return self.comment_text[:15] + "..."
        else:
            return self.comment_text
    get_comment_text.short_comment_text="Текст комментария"


class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категории')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0, validators=[MinValueValidator(1111111111), MaxValueValidator(9999999999)])
    city = models.CharField(max_length=20, blank=True )
    verification = models.BooleanField(default=False)
