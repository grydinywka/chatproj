from django.shortcuts import render
from django.views.generic.base import TemplateView


class EnterView(TemplateView):
    """
        View for serving home(index) page
    """

    template_name = 'index.html'
