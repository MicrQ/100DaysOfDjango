from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    """ signup page view """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
