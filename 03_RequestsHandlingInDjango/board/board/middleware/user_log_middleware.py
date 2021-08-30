from django.core.exceptions import PermissionDenied
import datetime

class UserLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        date = datetime.datetime.now()
        URL = request.path
        method = request.method
        with open('user_log.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{date}: {URL}, {method}')
        response = self.get_response(request)
        return response

