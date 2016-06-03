from __future__ import unicode_literals

from django.db import models


class Fact(models.Model):
    short_text = models.CharField(max_length=255)
    ref_link = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.short_text
