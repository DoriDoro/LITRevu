from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginView, RegisterView

app_name = 'accounts'

# TODO: redirect Logout to login_page.html

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base_layout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
