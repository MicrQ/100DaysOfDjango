from django.urls import reverse
from rest_framework import status
from books.models import Book
from rest_framework.test import APITestCase


class APITests(APITestCase):
    """ tests for the apis """

    @classmethod
    def setUpTestData(cls):
        """ setting up data used for testing """
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python and Django",
            author="William S. Vincent",
            isbn="9781735467221",
        )

    def test_api_listview(self):
        """ test to check the response of the api call """
        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
