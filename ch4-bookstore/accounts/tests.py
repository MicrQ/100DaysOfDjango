from django.urls import reverse, resolve
from django.test import TestCase
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from .views import SignupPageView


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


class SignUpPageTests(TestCase):
    """ tests dedicated to the signup page and functionality """

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        """ will be used to avoid redundency and repetition """
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        """ test to check if the right template is used """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be here.')

    def test_signup_form(self):
        """" test for the form used in the signup page """
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        
        # form = self.response.context.get('form')
        # self.assertIsInstance(form, CustomUserCreationForm)
        # self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        """ test for the signup page view """
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )
