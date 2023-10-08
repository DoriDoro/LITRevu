from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import CharField, Q, Value
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .forms import ReviewForm, ModifiedReviewForm
from .models import Ticket, Review


class FeedsView(LoginRequiredMixin, TemplateView):
    """All reviews and tickets on the feeds page"""

    template_name = "feeds/feeds_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tickets = (
            Ticket.objects.filter(reviews__isnull=True)
            .filter(
                Q(creator__followed_by__user=self.request.user)
                | Q(creator=self.request.user)
            )
            .distinct()
            .annotate(type_of_content=Value("TICKET", CharField()))
        )
        reviews = (
            Review.objects.filter(
                Q(author__followed_by__user=self.request.user)
                | Q(author=self.request.user)
                | Q(ticket__creator=self.request.user)
            )
            .distinct()
            .annotate(type_of_content=Value("REVIEW", CharField()))
        )
        context["posts"] = sorted(
            chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
        )

        return context


class CreateTicketView(LoginRequiredMixin, CreateView):
    """Button: 'Ask for a review' View. Create a new ticket"""

    model = Ticket
    fields = ["title", "description", "image"]
    template_name = "feeds/create_ticket_page.html"
    success_url = reverse_lazy("review:feeds_page")

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.creator = self.request.user
        form.save()

        return super().form_valid(form)


class CreateReviewView(LoginRequiredMixin, CreateView):
    """Button: 'Create a review' on the top of the feeds or posts page.
    You choose a ticket to review."""

    # TODO: limit the queryset to the tickets of followed users

    model = Review
    form_class = ReviewForm
    template_name = "feeds/create_review_page.html"
    success_url = reverse_lazy("review:feeds_page")

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        form.save()

        return super().form_valid(form)


class CreateReviewForTicketView(LoginRequiredMixin, CreateView):
    """Button 'Create a review' on a ticket without a review."""

    model = Review
    form_class = ModifiedReviewForm
    template_name = "feeds/create_review_for_ticket.html"
    success_url = reverse_lazy("review:feeds_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ticket"] = Ticket.objects.get(pk=self.kwargs.get("pk"))

        return context

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        review.ticket_id = self.kwargs["pk"]
        form.save()

        return super().form_valid(form)


class PostsView(LoginRequiredMixin, TemplateView):
    """All reviews and tickets on the feeds page"""

    template_name = "posts/posts_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.filter(creator=self.request.user)
        context["reviews"] = Review.objects.filter(author=self.request.user)
        return context


class PostsModifyReviewView(LoginRequiredMixin, UpdateView):
    """View to modify a review"""

    model = Review
    form_class = ReviewForm
    template_name = "posts/posts_modify_review_page.html"
    success_url = reverse_lazy("review:posts_page")


class PostDeleteReviewView(LoginRequiredMixin, DeleteView):
    """DeleteView to remove a Review"""

    model = Review
    template_name = "posts/delete_confirmation.html"
    success_url = reverse_lazy("review:posts_page")


class PostsModifyTicketView(LoginRequiredMixin, UpdateView):
    """View to modify a ticket"""

    model = Ticket
    fields = ["title", "description", "image"]
    template_name = "posts/posts_modify_ticket_page.html"
    success_url = reverse_lazy("review:posts_page")


class PostDeleteTicketView(LoginRequiredMixin, DeleteView):
    """DeleteView to remove a Review"""

    model = Ticket
    template_name = "posts/delete_confirmation.html"
    success_url = reverse_lazy("review:posts_page")
