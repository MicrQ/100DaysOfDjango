from django.test import TestCase
from .models import Todo


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
