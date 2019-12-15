from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from apps.accounts.views import SignUpView, UserUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update_user/<int:pk>/", UserUpdateView.as_view(), name="update_user"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

