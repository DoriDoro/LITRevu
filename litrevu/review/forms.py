from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Layout, Submit
from django import forms

from .models import Ticket


class TicketCreateForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

"""
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            Fieldset(
                "Create a ticket",
                'title',
                'description',
                'image',
            ),
            Div(
                Submit('submit', "Create this ticket"),
            ),
        )

        return helper
"""