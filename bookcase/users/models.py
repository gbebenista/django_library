from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy
from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(ugettext_lazy('username'), max_length=40, unique=True)
    email = models.EmailField(ugettext_lazy('email address'), unique=True)
    password = models.CharField(ugettext_lazy('password'), max_length=100)
    date_joined = models.DateTimeField(ugettext_lazy('date joined'), default=timezone.now)
    is_active = models.BooleanField(ugettext_lazy('active'), default=True)
    is_staff = models.BooleanField(ugettext_lazy('staff'), default=False)
    is_superuser = models.BooleanField(ugettext_lazy('admin'), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email

