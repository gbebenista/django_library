from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class LoginByEmailOrUsername(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(**{'email': username})
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
