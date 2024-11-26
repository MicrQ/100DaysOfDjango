from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    """ used to specify which fields to be displayed on the admin page """
    list_display = ('title', 'author', 'price')


# Register your models here.
admin.site.register(Book, BookAdmin)
