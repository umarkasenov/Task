from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, models


class RegistrationView(generic.CreateView):
    template_name = 'register_and_authorization/registration.html'
    form_class = forms.CustomRegistrationForm
    success_url = '/login/'


class AuthorizationView(LoginView):
    template_name = 'register_and_authorization/authorization.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse('users:greeting')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class GreetingView(generic.ListView):
    template_name = "register_and_authorization/greeting.html"
    context_object_name = 'greet'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()
