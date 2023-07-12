from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from .forms import LoginForm, RegisterForm


class LoginView(FormView):

    form_class = LoginForm
    template_name = 'login_page.html'

    def get_success_url(self):
        return reverse('review:review_page')

    def form_valid(self, form):
        return super().form_valid(form)


class RegisterView(FormView):

    form_class = RegisterForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)
