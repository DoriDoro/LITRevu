from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, View, CreateView

from .forms import LoginForm, RegisterForm


class LoginView(LoginView):
    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = "login_page.html"

    def get_success_url(self):
        return reverse("review:review_page")


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("review:review_page")

    # def get_success_url(self):
    #     return reverse("review:review_page")

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)
