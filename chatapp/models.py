from __future__ import unicode_literals

from django.db import models


class Notice(models.Model):
    content = models.TextField(blank=False, null=True, default=None)
    user = models.ForeignKey('auth.User', null=True, blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "# %s, user %s" % (self.id, self.user.username)
