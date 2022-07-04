from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppDjfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_djfiles'
    verbose_name = _('Новости')
