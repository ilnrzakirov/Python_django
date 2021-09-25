from django.contrib import admin
from .models import News, NewsComment
# Register your models here.


class NewsCommentInline(admin.TabularInline):
    model = NewsComment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'status']
    list_filter = ['status']

    inlines = [NewsCommentInline]

    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(status='a')

    def mark_as_inactive(self, request, queryset):
        queryset.update(status='i')

    mark_as_active.short_description= "Перевести в активно"
    mark_as_inactive.short_description= "Перевести в неактивно"

@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):

    list_display = ['id', 'username', 'get_comment_text', 'news']

    list_filter = ['username']

    actions = ['deleted_by_the_administrator']

    def deleted_by_the_administrator(self, request, queryset):
        queryset.update(comment_text="Удалено администратором")

    deleted_by_the_administrator.short_description = "Удалить"



