from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from .forms import LoginForm, RegisterForm


# def logout_user(request):
#     logout(request)
#     return redirect('home')


class HomeView(FormView):

    form_class = LoginForm
    template_name = 'homepage.html'

    def get_success_url(self):
        return reverse('register')

    def form_valid(self, form):
        return super().form_valid(form)


class RegisterView(FormView):

    form_class = RegisterForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)
