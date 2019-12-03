from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "phone_number", "address", "image")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number", "address", "image")
