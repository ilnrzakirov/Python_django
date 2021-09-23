from django.contrib import admin
from .models import News, NewsComment
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):
    pass