from django.db import models


class NewsStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name="Флаг активности")

    def __str__(self):
        return self.status


class News(models.Model):
    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'inactive'),
    ]
    name = models.CharField(max_length=1000, verbose_name="Название")
    description = models.CharField(max_length=1000, verbose_name="Содрежание", default='')
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='i')

    def __str__(self):
        return f'{self.name} {self.created_at} {self.status}'

    class Meta:
        ordering = ['name']


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")

    def __str__(self):
        return self.username


class NewsComment(models.Model):
    username = models.ForeignKey('User', default=None, null=True, verbose_name="Имя пользователя",
                                 on_delete=models.CASCADE)
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



