from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.accounts.models import User

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class UserUpdateView(UpdateView):
    form_class = CustomUserChangeForm
    queryset = User.objects.all()
    success_url = reverse_lazy("login")
    template_name = "accounts/update.html"