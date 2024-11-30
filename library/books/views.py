from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    """ view to display available books for user """

    model = Book
    template_name = 'bool_list.html'
