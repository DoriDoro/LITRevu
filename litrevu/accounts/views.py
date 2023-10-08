from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, DeleteView

from .forms import RegisterForm, AboForm
from .models import UserFollow, User


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("review:feeds_page")

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)


class AboFollowView(LoginRequiredMixin, FormView):
    """View for the abo page. Follow a user and list the users who are following the user"""

    # TODO: you are following this user already

    model = UserFollow
    form_class = AboForm
    template_name = "abo_page.html"
    success_url = reverse_lazy("accounts:abo_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["followed_users"] = self.request.user.following.all()
        context["followed_by_others"] = UserFollow.objects.filter(
            followed_user=self.request.user
        )

        return context

    def form_valid(self, form):
        if "follow" in form.data:
            user_to_follow = get_object_or_404(
                User, username=form.cleaned_data["search"]
            )
            user_follows = UserFollow(
                user=self.request.user, followed_user=user_to_follow
            )
            user_follows.save()

        else:
            return reverse_lazy("accounts:abo_page")

        return super().form_valid(form)


class AboUnfollowView(LoginRequiredMixin, DeleteView):
    """View to unfollow a user."""

    model = UserFollow
    fields = ["user"]
    template_name = "posts/delete_confirmation.html"
    success_url = reverse_lazy("accounts:abo_page")

    # def form_valid(self, form):
    #     if "unfollow" in form.data:
    #         print("unfollow", form.data)
    #         print("------", self.__dict__)
    # user_to_unfollow = get_object_or_404(User, id=form.data.get("unfollow"))
    # UserFollows.objects.get(
    #     user=self.request.user, followed_user=user_to_unfollow
    # ).delete()
