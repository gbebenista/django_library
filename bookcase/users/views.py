from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreation, UserLogin
from .managers import UserManager


class RegisterView(CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class ViewLogin(LoginView):
    form_class = UserLogin
    succes_url = reverse_lazy('logresult')
    template_name = 'registration/login.html'
