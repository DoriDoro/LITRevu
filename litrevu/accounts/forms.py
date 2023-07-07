from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, Layout, Submit

from .models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            Fieldset(
                "Your unique username",
                'username',
            ),
            ButtonHolder(
                Submit('submit', "Register")
            ),
        )

        return helper
