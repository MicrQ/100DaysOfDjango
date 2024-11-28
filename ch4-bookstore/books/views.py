from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    """ used to display give list of models """
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, DetailView):
    """ used to display the detail of a book model """
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'


class SearchResultListView(ListView):
    """ view for search results """
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
