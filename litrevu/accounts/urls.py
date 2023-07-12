from django.urls import path

from .views import HomeView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
