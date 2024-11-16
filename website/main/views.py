from django.shortcuts import render
from django.http import HttpResponse
""" views for the main app """


def home(request):
    """ home page || landing page """
    return render(request, 'main/home.html')
