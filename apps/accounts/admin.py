from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from apps.accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from apps.accounts.models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email','phone_number', 'address']

admin.site.register(User, CustomUserAdmin)