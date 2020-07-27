from django.contrib import admin
from django.contrib.auth.models import Group

from .forms import UserCreation, UserChange
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserAdministrator(UserAdmin):
    add_form = UserCreation
    form = UserChange
    model = CustomUser
    list_display = ['username', 'email', 'is_superuser', 'is_staff', 'is_active', ]
    list_filter = ('username',)
    fieldsets = (None, {'fields': ('username', 'email')}), ('Permissions', {'fields': ('is_active',
                                                                                                   'is_staff',
                                                                                                   'is_superuser', 'user_permissions')})


admin.site.register(CustomUser, UserAdministrator)
admin.site.unregister(Group)
