from django.urls import path
from . import views
""" url patterns for the polls app """


urlpatterns = [
    path('', views.index, name='index'),
]