from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django import forms


class UserCreation(UserCreationForm):
    email = forms.CharField()

    def clean_email(self):
        submitted_data = self.cleaned_data.get('email')
        domain_part = submitted_data.rsplit('@', 1)
        if domain_part[1] == 'doradigital.pl':
            return submitted_data
        raise forms.ValidationError('You must register using a @doradigital.pl address')


    class Meta:
        model = User
        fields = ('username', 'email')


class UserChange(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
