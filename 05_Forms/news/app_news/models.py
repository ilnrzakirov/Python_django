from django.db import models


class News(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Название")
    description = models.CharField(max_length=1000, verbose_name="Содрежание", default='')
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)
    status = models.ForeignKey('NewsStatus', default=None, null=True, verbose_name='Флаг активности',
                               on_delete=models.CASCADE, related_name='Status')
#    comment = models.ForeignKey("NewsComment", default=None, null=True, verbose_name="Коментарии",
#                                on_delete=models.CASCADE, related_name='Comment')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class NewsComment(models.Model):
    username = models.ForeignKey('User', default=None, null=True, verbose_name="Имя пользователя",
                                 on_delete=models.CASCADE, related_name='Username')
    comment_text = models.CharField(max_length=1000, default='')
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='News', null=True, verbose_name="новость",
                             default=None)

    def __str__(self):
        return self.comment_text

class NewsStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name="Флаг активности")

    def __str__(self):
        return self.status

class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")

    def __str__(self):
        return self.username