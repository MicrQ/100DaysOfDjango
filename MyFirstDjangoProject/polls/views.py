from django.shortcuts import render
from django.http import HttpResponse
""" My first and the most basic django view """


def index(request):
    """ handles the root page
        Args:
            request: HttpRequest object
        Return:
            HttpResponse with simple text
    """
    return HttpResponse("Welcome to polls app!")
