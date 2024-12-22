from django.test import TestCase
from django.contrib.auth import get_user_model


class AccountTests(TestCase):
    """ tests for user model """
    def test_user_model(self):
        """ test user model """
        User = get_user_model()
        user = User.objects.create_user(
            email="test@user.com",
            firstname="test",
            lastname="user",
            password="testpassword"
        )
        self.assertEqual(user.email, "test@user.com")
        self.assertEqual(user.firstname, "test")
        self.assertEqual(user.lastname, "user")
        self.assertFalse(user.is_staff, False)


class AccountViewsTests(TestCase):
    """ tests for account views """
    def test_user_registration_view(self):
        """ test user registration view """
        response = self.client.post(
            '/api/v1/accounts/register/',
            {
                'email': 'test@user.com',
                'firstname': 'test',
                'lastname': 'user',
                'password': 'testpassword'
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'],
                         'User registered successfully')
        self.assertTrue('token' in response.data)

    def test_user_login_view(self):
        """ test user login view """
        self.test_user_registration_view()
        response = self.client.post(
            '/api/v1/accounts/login/',
            {
                'email': 'test@user.com',
                'password': 'testpassword'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'],
                         'Logged in successfully')
        self.assertTrue('token' in response.data)

        return response.data['token']
