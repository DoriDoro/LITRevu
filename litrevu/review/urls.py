from django.urls import path

from .views import ReviewView, CreateTicketView

app_name = 'review'

urlpatterns = [
    path('review/', ReviewView.as_view(), name='review_page'),
    path('create_ticket/', CreateTicketView.as_view(), name='create_ticket'),
]
