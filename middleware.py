# task_manager/middleware.py

from django.shortcuts import redirect
from django.http import HttpResponse

class RedirectIfNotLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the user is not authenticated and is trying to access a page
        # other than the login or signup pages, redirect to the login page.
        if not request.user.is_authenticated and request.path not in ['/login/', '/register/']:
            return redirect('/login/')  # or another page of your choice
        return self.get_response(request)
