from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    """A ticket is related to a Review."""

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
        ordering = ["-ticket_created"]

    title = models.CharField(max_length=128, verbose_name=_("title of ticket"))
    description = models.TextField(
        max_length=2048, verbose_name=_("description"), blank=True
    )
    creator = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="ticket_creator",
        verbose_name=_("creator of ticket"),
    )
    image = models.ImageField(
        upload_to="images/", verbose_name=_("image"), blank=True, null=True
    )
    ticket_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("ticket created at")
    )

    def __str__(self):
        return f"{self.title} | {self.creator}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            img.thumbnail((250, 375))
            img.save(self.image.path)


class Review(models.Model):
    """A Review has a rating and a ticket."""

    # ONE_STAR = 1
    # TWO_STARS = 2
    # THREE_STARS = 3
    # FOUR_STARS = 4
    # FIVE_STARS = 5
    #
    # STARS_CHOICES = [
    #     (ONE_STAR, "1 star"),
    #     (TWO_STARS, "2 stars"),
    #     (THREE_STARS, "3 stars"),
    #     (FOUR_STARS, "4 stars"),
    #     (FIVE_STARS, "5 stars"),
    # ]

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        ordering = ["-review_created"]

    ticket = models.ForeignKey(
        "review.Ticket",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("ticket"),
    )
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name=_("rating"),
    )
    # rating = models.CharField(max_length=1, choices=STARS_CHOICES)
    headline = models.CharField(max_length=128, verbose_name=_("title of review"))
    body = models.TextField(verbose_name=_("comment"), blank=True)
    author = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="review_author",
        verbose_name=_("author"),
    )
    review_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("review created at")
    )

    def __str__(self):
        return str(self.headline)
