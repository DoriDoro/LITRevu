from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import RegisterForm


class RegisterView(FormView):

    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        pass
        # return redirect('register_confirmation')
