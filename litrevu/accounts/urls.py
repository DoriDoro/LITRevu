from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterView

app_name = "accounts"

urlpatterns = [
    path("", LoginView.as_view(template_name="login_page.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
