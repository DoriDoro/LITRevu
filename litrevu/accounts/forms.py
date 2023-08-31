from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Div, Fieldset, Layout, Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            Fieldset(
                "Login",
                "username",
                "password",
            ),
            Div(
                Submit("submit", "Login"),
            ),
        )

        return helper


class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        return user
