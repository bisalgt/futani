from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from apps.accounts.views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

