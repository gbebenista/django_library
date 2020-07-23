from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser


class UserCreation(UserCreationForm):

    def clean_email(self):
        submitted_data = self.cleaned_data.get('email')
        domain_part = submitted_data.rsplit('@', 1)
        if domain_part[1] == 'doradigital.pl':
            return submitted_data
        raise forms.ValidationError('You must register using a @doradigital.pl address')

    def save(self, commit=True):

        user = CustomUser.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    class Meta:
        model = CustomUser
        fields = ('email',)


class UserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class UserLogin(AuthenticationForm):

    class Meta:
        model = CustomUser