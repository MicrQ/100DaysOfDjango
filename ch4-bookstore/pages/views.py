from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """ landing page """
    template_name = 'home.html'


class AboutPageView(TemplateView):
    """ view for the static about page """
    template_name = 'about.html'
