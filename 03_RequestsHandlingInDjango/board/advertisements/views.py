import requests
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Advertisements

advertisements = [
    'Мастер на час',
    'Выведение из запоя',
    'Услуги экскаватора-погрузчика, гидромолота, ямобура',
    'Электрик'
]

# def advertisement_list(request, *args, **kwargs):
#     advertisements = Advertisements.object.all()
#     return render(request, 'advertisements/advertisements.html', {'advertisements': advertisements})

count = 0

class Advertisement(TemplateView):
    template_name = 'advertisements/advertisements.html'

    def get_context_data(self, **kwargs):
        global count
        count += 1
        context = super().get_context_data(**kwargs)
        context['list'] = advertisements
        context['views'] = count
        return context

    def post(self, **kwargs):
        return HttpResponse('Запрос на создание новой записи успешно выполнен')


class Contacts(TemplateView):
    template_name = 'advertisements/сontacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = 'Москва, Пушкина д1 89999999999, mail@mail.ru'
        return context

class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = 'Компания'
        context['about'] = "Какой то текст Какой то текст Какой то текст Какой то текст"
        return context

class Index(TemplateView):
    template_name = 'advertisements/advertisement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ['категория 1', 'категория 2']
        context['region'] = ['116', '777']
        return context

class AdvertisementsListView(ListView):
    model = Advertisements
    template_name = 'advertisements/advertisements_list_view.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisements.objects.all()[:8]


class AdvertisementDetailView(DetailView):
    model = Advertisements
    template_name = 'advertisements/advertisement_detail.html'