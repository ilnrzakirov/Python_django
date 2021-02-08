import random
from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        l1 = ['Установить python', 'Установить django', 'Запустить сервер', 'Написать код', 'Порадоваться результату',
              'Посмотреть что получилось', 'Порадоваться еще раз', 'Задать суперпользователя', 'Ввести пароль администратора', 'Ну еще что нибул сделать']
        response1 = random.sample(l1, 5)
        response = "<ul>"
        for i_team in response1:
            response += "<li>" +  i_team + "</li>"
        response +="</ul>"


        return HttpResponse(response)
