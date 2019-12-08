from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import AccountUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class AccountUserAdmin(UserAdmin):
    # fieldsets = UserAdmin.fieldsets + (
    #     (
    #         'Extra', {
    #             'fields': ('avatar', 'phone')
    #         }
    #     ),
    # )
    
    # использую другой вариант:

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = AccountUser
    list_display = ['email', 'username',]



admin.site.register(AccountUser,AccountUserAdmin)
