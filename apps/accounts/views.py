from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.accounts.models import User

class SignUpView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy("login")
#     template_name = "accounts/update.html" 

#     def get_object(self):
#         print(dir(self))
#         return get_object_or_404(User, id=self.request.user.id)


#     def test_func(self):
#         user = self.get_object()
#         if self.request.user.id == user.id:
#             return True
#         return False    
    
@login_required
def user_update(request, id, slug):
    if request.user.id == id:
        user = User.objects.get(id=id)
        form = CustomUserChangeForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, 'accounts/update.html', {'form':form})
    else:
        return render(request, 'forbidden.html')


@login_required
def user_detail(request, id, slug):
    if request.user.id == id:
        user = get_object_or_404(User, id=id)
        context = {'user':user}
        return render(request, 'accounts/user_detail.html', context)
    else:
        return render(request, 'forbidden.html')