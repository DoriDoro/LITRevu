from django.urls import path

from .views import (
    FeedsView,
    CreateTicketView,
    CreateReviewView,
    CreateReviewForTicketView,
    PostsView,
    PostsModifyReviewView,
    PostDeleteReviewView,
    PostsModifyTicketView,
    PostDeleteTicketView,
)

app_name = "review"

urlpatterns = [
    path("feeds/", FeedsView.as_view(), name="feeds_page"),
    path("create-ticket/", CreateTicketView.as_view(), name="create_ticket"),
    path("create-review/", CreateReviewView.as_view(), name="create_review"),
    path(
        "create-review-ticket/<int:pk>/",
        CreateReviewForTicketView.as_view(),
        name="create_review_ticket",
    ),
    path("posts/", PostsView.as_view(), name="posts_page"),
    path(
        "posts/modify-review/<int:pk>",
        PostsModifyReviewView.as_view(),
        name="modify_review",
    ),
    path(
        "posts/delete-review/<int:pk>/",
        PostDeleteReviewView.as_view(),
        name="delete_review",
    ),
    path(
        "posts/modify-ticket/<int:pk>",
        PostsModifyTicketView.as_view(),
        name="modify_ticket",
    ),
    path(
        "posts/delete-ticket/<int:pk>/",
        PostDeleteTicketView.as_view(),
        name="delete_ticket",
    ),
]
