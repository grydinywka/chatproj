from django.shortcuts import render
from django.contrib.auth.views import login
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class CustomLoginView(TemplateView):
    """
        View for login page
    """

    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('chat'))
        return login(request)
