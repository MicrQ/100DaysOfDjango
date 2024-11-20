from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """ tests for the home page templates """

    def test_url_exists_at_correct_location(self):
        """ test to check if the home url is working """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        """ test if the homepage's url name is pointing
            to the right path || endpoint
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        """ test to check if the right template is used """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
