from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fact(models.Model):
	short_text = models.CharField(max_length=255)

	def __unicode__(self):
		return "%s" %self.short_text
