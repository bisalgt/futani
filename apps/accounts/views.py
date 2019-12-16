from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.accounts.models import User

class SignUpView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("login")
    template_name = "accounts/update.html"

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)
        
        
@login_required
def user_detail(request, id, slug):
    user = get_object_or_404(User, id=id)
    context = {'user':user}
    return render(request, 'accounts/user_detail.html', context)