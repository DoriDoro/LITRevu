from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .forms import TicketForm, ReviewForm
from .models import Ticket, Review


class FeedsView(LoginRequiredMixin, TemplateView):
    template_name = "feeds_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()
        context["reviews"] = Review.objects.all()
        return context


class CreateTicketView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "create_ticket_page.html"
    success_url = reverse_lazy("review:feeds_page")

    def form_valid(self, form):
        # if form.is_valid:
        ticket = form.save(commit=False)
        ticket.creator = self.request.user
        form.save()

        return super().form_valid(form)


class CreateReviewView(LoginRequiredMixin, CreateView):
    form_class = ReviewForm
    template_name = "create_review_page.html"
    success_url = reverse_lazy("review:feeds_page")

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        form.save()

        return super().form_valid(form)
