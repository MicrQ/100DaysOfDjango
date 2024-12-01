from .models import Todo
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class TodoModelTest(TestCase):
    """ tests for the todo model """

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='First Todo',
            body='A body of the first todo'
        )

    def test_model_content(self):
        """ tests to check the todo model contents """
        self.assertEqual(self.todo.title, 'First Todo')
        self.assertEqual(self.todo.body, 'A body of the first todo')
        self.assertEqual(str(self.todo), 'First Todo')

    def test_api_listview(self):
        """ test to check the api list view """
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        """ test to check the api detail view """
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
