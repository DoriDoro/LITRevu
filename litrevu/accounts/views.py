from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.views.generic.edit import FormView

from .forms import LoginForm, RegisterForm


# authentication/views.py
from django.shortcuts import render

from . import forms


# def logout_user(request):
#     logout(request)
#     return redirect('home')


class HomeView(View):

    form_class = LoginForm
    template_name = 'homepage.html'

    def get(self, request):
        form = self.form_class
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Login failed!'

        return render(request, self.template_name, context={'form': form, 'message': message})


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
