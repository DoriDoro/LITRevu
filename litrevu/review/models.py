from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    """ A ticket is related to a Review. """
    title = models.CharField(max_length=128, verbose_name="titre du ticket")
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name="image")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="ticket crée le")


class Review(models.Model):
    """ A Review has a rating and a ticket. """
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name="ticket")
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="note"
    )
    headline = models.CharField(max_length=128, verbose_name="titre de la critique")
    body = models.TextField(blank=True, verbose_name="commentaire")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="critique crée le")


class UserFollows(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed',
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by',
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ['user', 'followed_user']
