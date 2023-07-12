from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import LoginForm, RegisterForm


class HomeView(TemplateView):

    form_class = LoginForm
    template_name = 'homepage.html'


class RegisterView(FormView):

    form_class = RegisterForm
    template_name = 'register.html'
    # success_url = 'accounts:home'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)
