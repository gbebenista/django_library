from django.contrib import admin
from .forms import UserCreation, UserChange
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserAdministrator(UserAdmin):
    add_form = UserCreation
    form = UserChange
    model = User
    list_display = ['email', 'username', ]

admin.site.unregister(User)
admin.site.register(User, UserAdministrator)
