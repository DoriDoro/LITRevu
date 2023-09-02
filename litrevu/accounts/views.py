from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView

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


# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = "register.html"
#     success_url = reverse_lazy("review:review_page")
#
#     def form_valid(self, form):
#         user = form.save()
#
#         if user:
#             login(self.request, user)
#
#         return super().form_valid(form)


class AboView(LoginRequiredMixin, FormView):
    """View for the abo page. Follow a user, lists all followed users"""

    model = UserFollows
    form_class = AboForm
    template_name = "abo_page.html"
    # success_url = reverse_lazy("accounts:abo_page")

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
        if "follow" in self.request.POST:
            to_be_followed_user = form.cleaned_data["search"]
            user_to_follow = User.objects.get(username=to_be_followed_user)
            UserFollows.objects.create(
                user=self.request.user, followed_user=user_to_follow
            )

        elif "unfollow" in self.request.POST:
            user_id = self.request.POST.get("unfollow")
            user_to_unfollow = User.objects.get(id=user_id)
            UserFollows.objects.get(
                user=self.request.user, followed_user=user_to_unfollow
            ).delete()

        else:
            return reverse_lazy("accounts:abo_page")

        return super().form_valid(form)
