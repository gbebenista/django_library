from django.urls import path
from django.views.generic import TemplateView

from .views import RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]

