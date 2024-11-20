from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    """ test for the custom user model """

    def test_create_user(self):
        """ test creating a new user using the custom user model """
        User = get_user_model()
        user = User.objects.create_user(
            username='will', email='will@example.com', password='pass@123'
        )

        # check if the user is created successfully
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """ test creating a new superuser using the custom user model """
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='pass@123'
        )

        # check if the superuser is created successfully
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
