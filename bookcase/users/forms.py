from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
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
        fields = ('username', 'email',)


class UserChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(Field(PrependedText('username', '<i class="fa fa-user"></i>', placeholder="Username")),
                                    Field(PrependedText('password', '<i class="fa fa-lock"></i>', placeholder="Password")),
                                    Submit('submit', 'Login'))

    class Meta:
        model = User
