from django.urls import path

from .views import (
    FeedsView,
    CreateTicketView,
    CreateReviewView,
    CreateReviewForTicketView,
)

app_name = "review"

urlpatterns = [
    path("feeds/", FeedsView.as_view(), name="feeds_page"),
    path("create_ticket/", CreateTicketView.as_view(), name="create_ticket"),
    path("create_review/", CreateReviewView.as_view(), name="create_review"),
    path(
        "create_review_ticket/<int:pk>/",
        CreateReviewForTicketView.as_view(),
        name="create_review_ticket",
    ),
]
