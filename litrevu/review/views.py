from django.shortcuts import render
from django.views.generic.base import TemplateView

# from articles.models import Article


class ReviewView(TemplateView):
    template_name = "review_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["latest_articles"] = Article.objects.all()[:5]
        return context
