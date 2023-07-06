from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    username = models.CharField(max_length=50, unique=True, verbose_name=_("user name"))
    email = models.EmailField(unique=True, verbose_name=_("email"))

    def __str__(self):
        return self.username


class UserFollows(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name=_("user")
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by',
        verbose_name=_("follower")
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        unique_together = ['user', 'followed_user']
