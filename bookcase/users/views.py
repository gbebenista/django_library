from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreation, UserLogin


class RegisterView(CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


class ViewLogin(LoginView):
    form_class = UserLogin
    succes_url = reverse_lazy('logresult')
    template_name = 'registration/login.html'

