"""chatproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.views.generic import CreateView

from chatapp.views import home, chat, addnotice
from user_auth.views import custom_login


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^chat/$', chat, name='chat'),
    url(r'^add_notice/$', addnotice, name='add_notice'),

    url(r'^admin/', admin.site.urls),

    # User Related urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^users/login/$', custom_login, name='auth_login'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='chat'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
]
