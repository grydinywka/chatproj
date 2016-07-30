from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class EnterView(TemplateView):
    """
        View for serving home(index) page
    """

    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('chat'))
        return super(EnterView, self).dispatch(request, *args, **kwargs)


def chatlist(request):
    return render(request,'chat.html', {})
