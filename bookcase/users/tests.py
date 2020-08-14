from django.test import TestCase
import pytest

from users.models import CustomUser


@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user('gbebenista2@interia.pl', 'zaqwsx123')
    assert CustomUser.objects.count() == 1
