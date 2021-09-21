from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Advertisements


class AdvertisementsListView(ListView):
    model = Advertisements
    template_name = 'advertisements/advertisements.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisements.objects.all()


class AdvertisementDetailView(DetailView):
    model = Advertisements
    template_name = 'advertisements/advertisement_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj