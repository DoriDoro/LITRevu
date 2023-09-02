from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse

from .forms import TicketForm, ReviewForm
from .models import Ticket, Review


class FeedsView(LoginRequiredMixin, TemplateView):
    """All reviews and tickets on the feeds page"""

    template_name = "feeds/feeds_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()
        context["reviews"] = Review.objects.all()
        return context


class CreateTicketView(LoginRequiredMixin, CreateView):
    """Button: 'Ask for a review' View. Create a new ticket"""

    model = Ticket
    form_class = TicketForm
    template_name = "feeds/create_ticket_page.html"
    success_url = reverse_lazy("review:feeds_page")

    def form_valid(self, form):
        # if form.is_valid:
        ticket = form.save(commit=False)
        ticket.creator = self.request.user
        form.save()

        return super().form_valid(form)


class CreateReviewView(LoginRequiredMixin, CreateView):
    """Button: 'Create a review' on the top of the page. You choose a ticket to review."""

    model = Review
    form_class = ReviewForm
    template_name = "feeds/create_review_page.html"
    success_url = reverse_lazy("review:feeds_page")

    # TODO: display just the tickets without a review attached!
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[]

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        form.save()

        return super().form_valid(form)


class CreateReviewForTicketView(LoginRequiredMixin, CreateView):
    """Button 'Create a review' on a ticket without a review."""

    # TODO: display the image of ticket
    # TODO: remove ticket ChoiceField from ReviewForm
    # TODO: possible to remove a field from form?
    # TODO: possible to change the model of Review

    model = Review
    form_class = ReviewForm
    template_name = "feeds/create_review_for_ticket.html"
    success_url = reverse_lazy("review:feeds_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ticket"] = Ticket.objects.get(pk=self.kwargs.get("pk"))

        return context

    def form_valid(self, form):
        print("here---", form.instance.ticket_id)
        form.instance.ticket_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("create_review_ticket", kwargs={"pk": self.object.ticket.pk})


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
