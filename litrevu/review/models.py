from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    """ A ticket is related to a Review. """

    class Meta:
        verbose_name = "ticket"
        verbose_name_plural = "tickets"
        ordering = ["-ticket_created"]

    title = models.CharField(max_length=128, verbose_name="title of ticket")
    description = models.TextField(max_length=2048, verbose_name="description", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="creator of ticket",
    )
    # missing: upload_to= and storage=
    image = models.ImageField(verbose_name="image", blank=True, null=True)
    ticket_created = models.DateTimeField(auto_now_add=True, verbose_name="ticket created at")

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        """ return reverse("<path_to_urls.py_file>:<name_of_path>, kwargs={"pk": self.pk} """
        pass


class Review(models.Model):
    """ A Review has a rating and a ticket. """

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        ordering = ["-review_created"]

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name="ticket")
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="rating"
    )
    headline = models.CharField(max_length=128, verbose_name="title of review")
    body = models.TextField(verbose_name="comment", blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="author",
    )
    review_created = models.DateTimeField(auto_now_add=True, verbose_name="review created at")

    def __str__(self):
        return str(self.headline)

    def get_absolute_url(self):
        """ return reverse("<path_to_urls.py_file>:<name_of_path>, kwargs={"pk": self.pk} """
        pass
