from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Review, Ticket


class ReviewView(TemplateView):
    template_name = "review_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['tickets'] = Ticket.objects.all()
        return context
