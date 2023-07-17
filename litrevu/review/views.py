from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .forms import TicketCreateForm
from .models import Review, Ticket


class ReviewView(TemplateView):

    template_name = "review_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['tickets'] = Ticket.objects.all()
        return context


# login must be required, need a User instance for Ticket.creator
# Warning in console: `Cookie “csrftoken” has been rejected for invalid domain.`
class CreateTicketView(LoginRequiredMixin, CreateView):

    form_class = TicketCreateForm
    template_name = "create_ticket_page.html"
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        
        return super().form_valid(form)


"""
def image_upload_view(request):
    if request.method == 'POST':
        form = TicketCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'review:create_ticket_page', {'form': form, 'img_obj': img_obj})
    else:
        form = TicketCreateForm()

    return render(request, 'review:review_page', {'form': form})



class CreateTicketView(FormView):
    
    form_class = TicketCreateForm
    template_name = 'create_ticket_page.html'
    
    def get_success_url(self):
        return reverse('review:review_page')
    
    def form_valid(self, form):
        return super().form_valid(form)
"""
