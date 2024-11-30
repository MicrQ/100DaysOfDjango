from django.test import TestCase
from .models import Book
from django.urls import reverse


class BookTests(TestCase):
    """ test for the books app and its functionalities """

    @classmethod
    def setUpTestData(cls):
        """ setting up data to use for tests """

        cls.book = Book.objects.create(
            title='A good title',
            subtitle='An excellent subtitle',
            author='Tom',
            isbn='32454657898',
        )

    def test_book_content(self):
        """ test to check if the write data of the book is saved """
        self.assertEqual(self.book.title, 'A good title')
        self.assertEqual(self.book.subtitle, 'An excellent subtitle')
        self.assertEqual(self.book.author, 'Tom')
        self.assertEqual(self.book.isbn, '32454657898')

    def test_book_list_view(self):
        """ test to check the view of the books app """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'An excellent subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')
