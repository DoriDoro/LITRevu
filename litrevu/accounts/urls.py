from django.urls import path

from .views import RegisterView, login_page

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', login_page, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]
