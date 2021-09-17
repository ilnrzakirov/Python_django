from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Advertisements


class AdvertisementsListView(ListView):
    model = Advertisements
    template_name = 'advertisements/advertisements.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisements.objects.all()[:8]


class AdvertisementDetailView(DetailView):
    model = Advertisements
    template_name = 'advertisements/advertisement_detail.html'