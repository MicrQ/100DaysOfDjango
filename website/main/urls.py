from django.urls import path
from . import views
""" route defenitions for the main app """


urlpatterns = [
    path('', views.home, name='home'),
]
