"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from users.views import ViewLogin

urlpatterns = [
    path('', ViewLogin.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('signup/', include('users.urls')),
    path('password-reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('logresult/', TemplateView.as_view(template_name='users/logresult.html'), name='logresult')
]
