from django.db import DatabaseError
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class DatabaseErrorMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, DatabaseError):
            return HttpResponse({"Database not responding, please try again later."}, status=500)
