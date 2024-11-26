from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    """ used to make the review be displayed on the admin page """
    model = Review


class BookAdmin(admin.ModelAdmin):
    """ used to specify which fields to be displayed on the admin page """
    inlines = [
        ReviewInline,
    ]
    list_display = ('title', 'author', 'price')


# Register your models here.
admin.site.register(Book, BookAdmin)
