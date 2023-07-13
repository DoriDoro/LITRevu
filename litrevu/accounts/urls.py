from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginView, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='logout_page.html',
        next_page=None), name='logout'
    ),
    path('register/', RegisterView.as_view(), name='register'),
]
