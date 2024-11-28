from django.urls import reverse
from django.test import TestCase
from .models import Book, Review
from django.contrib.auth import get_user_model


# Create your tests here.
class BookTests(TestCase):
    """ test for the book model and its functionality """

    @classmethod
    def setUpTestData(cls):
        """ adds sample book to test thoughout the tests """
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='test123',
            email='user@test.com')

        cls.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        cls.review = Review.objects.create(
            book = cls.book,
            review = 'An excellent book',
            author = cls.user)

    def test_book_listing(self):
        """ test to check list of books """
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.price}', '25.00')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')

    def test_book_list_view(self):
        """ test to check view of books """
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        """ test to check the book detail functionality """
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/1234')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent book')
        self.assertTemplateUsed(response, 'books/book_detail.html')
