from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView

from .forms import RegisterForm


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
