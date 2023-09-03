from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, UserFollows


class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class AboForm(forms.Form):
    """form for the abo page, to follow and unfollow users"""

    search = forms.CharField(max_length=50, label=False)

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_search(self):
        search = self.cleaned_data["search"]

        # impossible to follow yourself:
        if self.user and self.user.username == search:
            raise forms.ValidationError("You can not follow yourself!")

        # impossible to follow an admin/superuser:
        if User.objects.filter(username=search, is_superuser=True).exists():
            raise forms.ValidationError("Please choose an other name to follow!")

        return search
