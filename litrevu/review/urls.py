from django.urls import path

from .views import FeedsView, CreateTicketView

app_name = "review"

urlpatterns = [
    path("feeds/", FeedsView.as_view(), name="feeds_page"),
    path("create_ticket/", CreateTicketView.as_view(), name="create_ticket"),
]
