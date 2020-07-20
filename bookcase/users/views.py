from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreation


class RegisterView(CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'

