import random
from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        l1 = ['Установить python', 'Установить django', 'Запустить сервер', 'Написать код', 'Порадоваться результату',
              'Посмотреть что получилось', 'Порадоваться еще раз', 'Задать суперпользователя']
        response = "<ul><li>" + random.choice(l1) + "</li><li>" + random.choice(l1) + '</li><li>' + random.choice(l1) + '</li><li>' + random.choice(l1) + '</li><li>' + random.choice(l1) + '</li></ul>'


        return HttpResponse(response)
