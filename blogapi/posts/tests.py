from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):
    """ tests for the blog model and its functionality """

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@user.com',
            password='secret',
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='A test title',
            body='Nice body content',
        )

    def test_post_model(self):
        """ test to check if the created post is the exact one """
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'A test title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(str(self.post), 'A test title')
