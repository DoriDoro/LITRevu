from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Div, Fieldset, Layout, Submit

from .models import User


class LoginForm(forms.Form):
    pass


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # TODO: use jQuery to verify the email and username
    #  in the form and not aver submitting the form
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "This username is already taken. Please choose an other username."
            )
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            # TODO: link to login
            raise forms.ValidationError(
                "This email address is already linked to an account."
                "Please login here."
            )
        return email

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            Fieldset(
                "Register here",
                'username',
                'email',
                'password1',
                'password2',
            ),
            Div(
                Submit('submit', "Register"),
                Button('cancel', "Cancel", css_class='btn-grey'),
                css_class='btns'
            ),
        )

        return helper
