from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.forms import forms


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if not user.email.split('@')[1] == "doradigital.pl":
            raise forms.ValidationError('You must register using a @doradigital.pl address')
