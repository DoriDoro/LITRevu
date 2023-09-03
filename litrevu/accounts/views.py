from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView

from .forms import RegisterForm, AboForm
from .models import UserFollows, User


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("review:review_page")

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)


# TODO: not working
class AboFollowView(LoginRequiredMixin, FormView):
    """View for the abo page. Follow a user"""

    model = UserFollows
    form_class = AboForm
    template_name = "abo_page.html"
    success_url = reverse_lazy("accounts:abo_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["followed_users"] = self.request.user.following.all()
        context["followed_by_others"] = UserFollows.objects.filter(
            followed_user=self.request.user
        )
        context["users"] = (
            User.objects.filter(
                is_superuser=False,
            )
            .exclude(
                id__in=self.request.user.following.values_list(
                    "followed_user_id", flat=True
                )
            )
            .exclude(id=self.request.user.id)
        )

        return context

    def form_valid(self, form):
        print("here-----", form.data)
        if "follow" in form.data:
            user_to_follow = get_object_or_404(
                User, username=form.cleaned_data["search"]
            )
            user_follows = UserFollows(
                user=self.request.user, followed_user=user_to_follow
            )
            user_follows.save()

        else:
            return reverse_lazy("accounts:abo_page")

        return super().form_valid(form)


class AboUnfollowView(LoginRequiredMixin, UpdateView):
    """View to unfollow a user and list the users how are following the user."""

    model = UserFollows
    fields = ["user"]
    # template_name = "abo_page_unfollow.html"
    success_url = reverse_lazy("accounts:abo_page")

    def get_context_data(self, **kwargs):
        print("lets see -------", self.object)

    """
            elif "unfollow" in form.data:
            print("unfollow", form.data)
            user_to_unfollow = get_object_or_404(User, id=form.data.get("unfollow"))
            UserFollows.objects.get(
                user=self.request.user, followed_user=user_to_unfollow
            ).delete()

            if form.error:
                print("errors", form.errors)
    """
