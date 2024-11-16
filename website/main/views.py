from django.shortcuts import render
from django.http import HttpResponse
""" views for the main app """


def home(request):
    """ home page || landing page """
    return HttpResponse('<h1>Hello, World!</h1>')
