from django.contrib import admin
from .models import Advertisements
# Register your models here.


@admin.register(Advertisements)
class AdvertisementsAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

# Register your models here.
