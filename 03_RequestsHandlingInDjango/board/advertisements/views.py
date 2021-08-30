import requests
from django.shortcuts import render
from django.views.generic import TemplateView

advertisements = [
    'Мастер на час',
    'Выведение из запоя',
    'Услуги экскаватора-погрузчика, гидромолота, ямобура',
    'Электрик'
]

def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1})

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
