from django.contrib import admin
from .models import Question
""" a module used to register models to make
    them available on the admin interface
"""


admin.site.register(Question)