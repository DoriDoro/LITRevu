from django.urls import path

from .views import ReviewView

app_name = 'review'

urlpatterns = [
    path('review/', ReviewView.as_view(), name='review_page'),
]
