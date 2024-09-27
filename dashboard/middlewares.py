from typing import Any
from django.http import HttpResponse
import datetime

class TimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        current_time = datetime.datetime.now().time()

        start_time = datetime.time(9, 0, 0)
        end_time = datetime.time(18, 0, 0)

        if not (start_time <= current_time <= end_time):
            return HttpResponse('The website is only available between 9am and 6pm')

        response = self.get_response(request)
        return response