from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegisterForm

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = True
        user.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserListView(ListView):
    model = User
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
