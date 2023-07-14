from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
# from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    """ A ticket is related to a Review. """

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
        ordering = ["-ticket_created"]

    title = models.CharField(max_length=128, verbose_name=_("title of ticket"))
    description = models.TextField(max_length=2048, verbose_name=_("description"), blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("creator of ticket"),
    )
    image = models.ImageField(upload_to='images', verbose_name=_("image"), blank=True, null=True)
    ticket_created = models.DateTimeField(auto_now_add=True, verbose_name=_("ticket created at"))

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        """ return reverse("<path_to_urls.py_file>:<name_of_path>, kwargs={"pk": self.pk} """
        pass


class Review(models.Model):
    """ A Review has a rating and a ticket. """

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        ordering = ["-review_created"]

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name=_("ticket"))
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name=_("rating")
    )
    headline = models.CharField(max_length=128, verbose_name=_("title of review"))
    body = models.TextField(verbose_name=_("comment"), blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("author"),
    )
    review_created = models.DateTimeField(auto_now_add=True, verbose_name=_("review created at"))

    def __str__(self):
        return str(self.headline)

    def get_absolute_url(self):
        """ return reverse("<path_to_urls.py_file>:<name_of_path>, kwargs={"pk": self.pk} """
        pass
