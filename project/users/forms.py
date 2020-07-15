from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserCreation(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserChange(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)
