from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """create User instance"""

    pass


class UserFollow(models.Model):
    """Model to identify which user is following whom"""

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name=_("user"),
    )
    followed_user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="followed_by",
        verbose_name=_("follower"),
    )

    def __str__(self):
        return f"{self.user} <{self.followed_user}>"

    class Meta:
        unique_together = ["user", "followed_user"]
