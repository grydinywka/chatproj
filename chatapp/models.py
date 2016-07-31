from __future__ import unicode_literals

from django.db import models


class Notice(models.Model):
    content = models.CharField(max_length=254, blank=False, null=True, default=None)
    user = models.ForeignKey('auth.User', null=True, blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return "# %s, user %s" % (self.id, self.user.username)
