from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Notice


class EnterView(TemplateView):
    """
        View for serving home(index) page
    """

    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('chat'))
        return super(EnterView, self).dispatch(request, *args, **kwargs)


class ChatView(ListView):
    model = Notice
    queryset = Notice.objects.all()
    template_name = 'chat.html'
    context_object_name = 'notices'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChatView, self).dispatch(request, *args, **kwargs)
