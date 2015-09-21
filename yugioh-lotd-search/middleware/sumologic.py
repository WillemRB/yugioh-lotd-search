import requests

from os import getenv
from time import time

class SumoLogicMiddleware(object):
    def process_request(self, request):
        request.META['sumologic_timestamp'] = time()
        return None

    def process_response(self, request, response):
        status = response.status_code
        contentlength = len(response.content)
        
        self.log(request, status, contentlength)
        return response

    def log(self, request, status, contentlength):
        elapsed = -1
        if 'sumologic_timestamp' in request.META:
            start = request.META['sumologic_timestamp']
            elapsed = int((time() - start) * 1000)

        source_ip = '0.0.0.0'
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            source_ip = request.META['HTTP_X_FORWARDED_FOR']

        method = request.method
        path = request.get_full_path()

        user = '-'
        if request.user.is_authenticated():
            user = request.user.get_username()

        payload = "{} {} {} {} {} {} {}".format(source_ip, user, method, path, status, contentlength, elapsed)

        r = requests.post(getenv('SUMOLOGIC_COLLECTOR_URL'), data=payload)
