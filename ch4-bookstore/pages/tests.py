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


class AboutPageTests(SimpleTestCase):
    """ tests for the static about page """

    def setUp(self):
        """ used to avoid redundency by loading necessary resources first """
        self.response = self.client.get(reverse('about'))

    def test_aboutpage_status_code(self):
        """ test to check if the about page is available on the
            expected endpoint.
        """
        self.assertEqual(200, self.response.status_code)

    def test_aboutpage_template(self):
        """ test to check if the about page is using the right template """
        self.assertTemplateUsed('about.html')

    def test_aboutpage_contains_correct_html(self):
        """ test to check if the page contains the expected html response """
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        """ test to check if the html response dosen't contain
            unexpected response
        """
        self.assertNotContains(self.response, 'Hi there! I should not be here')
