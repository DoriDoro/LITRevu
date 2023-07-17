import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from django.views.generic.edit import FormView

from .forms import LoginForm, RegisterForm


# create a logger instance:
logger = logging.getLogger(__name__)


class LoginView(FormView):

    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = 'login_page.html'

    def get_success_url(self):
        return reverse('review:review_page')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # login successful
            logger.info(f" User '{username}' logges in successfully.")

        # TODO: no message displayed on terminal
        else:
            logger.info(f" Failed login attempt for user '{username}'.")

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
