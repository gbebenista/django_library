from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('overview', views.TemplateView.as_view(template_name='books/overview.html'), name='overview'),
]