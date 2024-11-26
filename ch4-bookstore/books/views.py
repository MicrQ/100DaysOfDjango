from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.
class BookListView(ListView):
    """ used to display give list of models """
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    """ used to display the detail of a book model """
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
