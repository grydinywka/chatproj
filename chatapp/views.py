import datetime
import time

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Notice


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('chat'))
    return render(request, 'index.html', {})


@login_required
def chat(request):
    return render(request, 'chat.html', {'notices': Notice.objects.all()})


def addnotice(request):
    if request.method == 'POST':
        if request.POST.get('add_notice') is not None:
            content = request.POST.get('content')
            user = request.user

            if content != '':
                notice = Notice(content=content, user=user)
                notice.save()
                return JsonResponse({'content': content, 'username': user.username, 'created': time.strftime(
                    '%Y-%b-%d %H:%M:%S')})

            else:
                return JsonResponse({'content_error': 'Message is required!'})

    return HttpResponseRedirect(reverse('chat'))

