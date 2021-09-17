from django.contrib import admin
from .models import Advertisements
# Register your models here.


@admin.register(Advertisements)
class AdvertisementsAdmin(admin.ModelAdmin):
    pass

