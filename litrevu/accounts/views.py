from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import FormView

from .forms import RegisterForm


class RegisterView(FormView):

    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)
        # return redirect('register_confirmation')
