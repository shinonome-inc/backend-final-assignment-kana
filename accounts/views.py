from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import SignupForm
from .models import User


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/userprofile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
