from django.contrib import admin
from .models import Blog, Profile


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'created_at']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'verification']
