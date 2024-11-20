from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """ tests for the home page templates """

    def setUp(self):
        """ will be used to avoid redundency and repetition """
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        """ test to check if the home url is working """
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        """ test if the homepage's url name is pointing
            to the right path || endpoint
        """
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """ test to check if the right template is used """
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        """ test to check if the response contains
            the expected html
        """
        self.assertContains(self.response, 'home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        """ test to check if the response does not contain
            the unexpected html
        """
        self.assertNotContains(self.response, 'Hi there! I should not be here.')
