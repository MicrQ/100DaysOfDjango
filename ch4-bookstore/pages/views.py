from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """ landing page """
    template_name = 'home.html'
