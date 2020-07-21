from django.urls import path
from .views import RegisterView, ViewLogin

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]

