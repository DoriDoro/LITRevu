from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
